#!/usr/bin/env python

from fractions import Fraction
from functools import reduce
from getpass import getpass
from pprint import pprint
from shutil import rmtree
from subprocess import TimeoutExpired
from sys import stderr
from urllib.error import HTTPError
import argparse
import atexit
import base64
import configparser
import json
import os
import signal
import subprocess
import sys
import time
import urllib.request, urllib.parse

# Coursera API for External Grader Queues
class CourseraQueue:
    def __init__(self, queue_name, session_name, api_key):
        self.queue_name = queue_name
        self.session_name = session_name
        self.api_key = api_key

    # Forms a HTTP POST/GET with the given url and data.  Sends it and returns the resulting parsed JSON object.
    def __retrieve_json_response__(self, url, data = None):
          req = urllib.request.Request(url, data, { 'x-api-key' : self.api_key })
          return json.loads(urllib.request.urlopen(req).readall().decode('utf-8'))

    # Returns a submission from the queue if one exists, returns None otherwise.
    # Raises a URLError on an error.
    def pull_submission(self):
          url = 'https://class.coursera.org/%s/assignment/api/pending_submission?queue=%s' % (self.session_name, self.queue_name)
          resp = self.__retrieve_json_response__(url)
          if 'submission' in resp and resp['submission']:
              return resp['submission']

    # Post the given score and feedback along with the option deadline
    # feedbacks.  api_state should be the key given in the submission
    # for which this posted score is for.
    # Return True on success, False otherwise.
    def post_score(self, api_state, score, feedback, feedback_after_soft_close_time = '', feedback_after_hard_deadline = ''):
        url = 'https://class.coursera.org/%s/assignment/api/score' % self.session_name
        values = { 'api_state' : api_state,
                   'score' : score,
                   'feedback' : feedback,
                   'feedback_after_hard_deadline' : feedback_after_hard_deadline,
                   'feedback_after_soft_close_time' : feedback_after_soft_close_time }
        data = urllib.parse.urlencode(values).encode('utf-8')
        try:
            response = self.__retrieve_json_response__(url, data)
            return int(response['status']) == 202
        except:
            print('ERROR: %s' % sys.exc_info()[1], file=stderr)
            return False

    # Returns the length of the queue.
    # Raises a URLError on an error.
    def length(self):
          url = 'https://class.coursera.org/%s/assignment/api/queue_length?queue=%s' % (self.session_name, self.queue_name)
          resp = self.__retrieve_json_response__(url)
          return int(resp['queue_length'])

# Parse command line arguments and return them.
def parse_cmd_args():
    filepath = lambda p: os.path.abspath(os.path.expanduser(p)) # Convert string to absolute filepath.
    usage = '''harness.py (--local | --queue <queue> --session <session>)
                  [--submissions <dir>] [--resources <dir>] [--api-key <key>]
                  [--wait <secs>] [-N <num>] [-h] [-v] [--cleanup] [--length] [--pid <file>]'''
    parser = argparse.ArgumentParser(description='UW Coursera Grading Harness', usage=usage,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Print more logging messages.')
    parser.add_argument('--local', action='store_true',
                        help='Grade local submissions.')
    parser.add_argument('--submissions', default='submissions',
                        type=filepath,
                        help='Path to submissions')
    parser.add_argument('--resources', default='~/resources',
                        type=filepath,
                        help='Path to resources (Makefile, config, scripts, etc.)')
    parser.add_argument('--cleanup', action='store_true',
                        help='Cleanup generated files after grading a submission')
    parser.add_argument('-N', type=int,
                        help='Number of submissions to grade before stopping.')
    parser.add_argument('--pid', type=filepath,
                        help='File location for placing pid.')
    external_options = parser.add_argument_group('External Grader')
    external_options.add_argument('--queue',
                                  help='Queue for assignment')
    external_options.add_argument('--session',
                                  help='Coursera Session Name')
    external_options.add_argument('--api-key',
                                  help='Coursera API Key')
    external_options.add_argument('--length', action='store_true',
                                  help='Print queue length and exit.')
    external_options.add_argument('--wait', default=10, type=int,
                                  help='Time to wait between polling for new submissions')
    args = parser.parse_args()

    if not args.local and not (args.queue and args.session):
        parser.error('External grader options --queue and --session not specified.')
    elif args.local and (args.queue or args.session or args.api_key or args.length):
        parser.error('Local grader option selected but external grader arguments specified.')
    elif args.N != None and args.N < 1:
        parser.error('N must be a positive number.')

    return args

# Force creation of a directory unless it already exists.
os.path.makedirsf = lambda path: os.makedirs(path) if not os.path.isdir(path) else None
# Remove path iff it exists.
os.removef = lambda path: os.remove(path) if os.path.exists(path) else None

# TODO Errors and specification
def read_part_config(resources_dir, part_id):
    parser = configparser.SafeConfigParser({'grademult': '1',
                                            'timelimit': '5',
                                            'max-filesize': '4',
                                            'minimum-score': '0',
                                            'maximum-score': '100'})
    config_path = os.path.join(resources_dir, str(part_id), 'config')
    if verbose:
        print('Reading configuration from: %s' % config_path)
    parser.read(config_path)
    try:
        part_config = {'grademult': Fraction(parser.get('config', 'grademult')),
                       'minimum-score': Fraction(parser.get('config', 'minimum-score')),
                       'maximum-score': Fraction(parser.get('config', 'maximum-score')),
                       'timelimit': parser.getint('config', 'timelimit'),
                       'max-filesize': parser.getint('config', 'max-filesize'),
                       'filename': parser.get('config', 'filename'),
                       'resources': os.path.join(resources_dir, str(part_id))}
        if verbose:
            pprint(part_config)
            print()
        return part_config
    except:
        print('ERROR: %s. (%s)' % (sys.exc_info()[1], config_path), file=stderr)
        print(file=stderr)

def grade_submission_code(submission_dir, config, submission_code, cleanup=False):
    # Set up the student source directory
    srcpath = os.path.join(submission_dir, 'src')
    os.path.makedirsf(srcpath)

    # Save submission code
    filepath = os.path.join(srcpath, config['filename'])
    try:
        with open(filepath, 'w') as f:
            f.write(submission_code)

        filesize = int(os.stat(filepath).st_size)/1024
        if filesize > config['max-filesize']:
            os.remove(filepath)
            feedback =  'Your submission exceeds the maximum filesize and will not be graded.\n'
            feedback += 'Your submission size: %dKB.\nMaximum submission size: %dKB.\n' % (filesize, config['max-filesize'])
            return feedback
    except IOError:
        print('ERROR: %s' % sys.exc_info()[1], file=stderr)
        return False

    # Do the local grading
    results = grade_local_submission(submission_dir, config, cleanup=False)

    # Cleanup and exit
    if cleanup:
        rmtree(submission_dir)
    return results

def grade_local_submission(submission_dir, config, cleanup=False):
    def timeout_handler(signum, frame):
        raise TimeoutExpired('grade_submission', config['timelimit'])

    # Setup submission binary/output directories.
    bin_path = os.path.join(submission_dir, 'bin')
    out_path = os.path.join(submission_dir, 'out')
    os.path.makedirsf(bin_path)
    os.path.makedirsf(out_path)

    # Form the actual make commands
    makefile = os.path.join(config['resources'], 'Makefile')
    make_cmd = ['make', '-sf', makefile,
                '-C', submission_dir, 'RESOURCE_HOME=%s' % config['resources']]
    run_cmd = make_cmd[:] # Copy original make_cmd
    run_cmd.append('run')

    try:
        # Start the Timer
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(config['timelimit'])

        try:
            compile_log = os.path.join(submission_dir, 'out', 'compile.log')
            run_log = os.path.join(submission_dir, 'out', 'run.log')
            os.removef(compile_log)
            os.removef(run_log)

            # Compile submission
            execute_make_cmd(make_cmd, config['timelimit'], compile_log)
            # Run submission
            execute_make_cmd(run_cmd, config['timelimit'], run_log)
        except subprocess.CalledProcessError: # make returned an error code
            signal.alarm(0)
            (log, feedback) =\
                (run_log, 'Could not run submission tests') if os.path.isfile(run_log) else (compile_log, 'Could not compile submission')
            with open(log, 'r') as f:
                feedback += ':\n' + f.read()
            return feedback
        except TimeoutExpired: raise
        except:
            signal.alarm(0)
            print('ERROR: %s' % sys.exc_info()[1], file=stderr)
            return False

        # Tests complete
        signal.alarm(0)

        # Parse tests log
        tests_log = os.path.join(submission_dir, 'out', 'tests.log')
        try:
            log = ""
            with open(tests_log, 'r') as f:
                log = f.read()
            (score, feedback) = parse_feedback(log)
        except IOError:
            print('ERROR: %s' % sys.exc_info()[1], file=stderr)
            if not os.path.exists(tests_log):
                print('  Make sure test scripts generate the file.', file=stderr)
            return False
        except TimeoutExpired: raise
        except:
            print('ERROR: %s' % sys.exc_info()[1], file=stderr)
            print('Grading script output malformatted:', file=stderr)
            pprint(log, stream=stderr)
            return False

        # Finished grading successfully, return results
        return {'score': score, 'feedback': feedback}
    except TimeoutExpired:
        return 'The submission exceeded the allotted grading time.\n'
    finally:
        if cleanup:
            rmtree(bin_path)
            rmtree(out_path)

def parse_feedback(feedback):
    feedback = feedback.splitlines()

    test_results = map(lambda l: l.split(';', 1), feedback)
    return reduce(lambda s_f, ts_tf: # TODO Cleanup
                  (s_f[0]+Fraction(ts_tf[0]),
                   s_f[1]+ts_tf[1]+'\n' if ts_tf[1].strip() != '' else s_f[1]),
                  test_results, (0, ''))

def execute_make_cmd(cmd, timeout=None, log_file='make.log'):
    def preexec():
        os.setpgrp()
    with open(log_file, 'w') as outf:
        with open(os.devnull, 'w') as null:
            with subprocess.Popen(cmd, stdout=outf, stderr=null, preexec_fn=preexec) as proc:
                try:
                    returncode = proc.wait(timeout=timeout)
                    if returncode != 0:
                        raise subprocess.CalledProcessError(returncode, cmd)
                except subprocess.CalledProcessError: raise
                except:
                    os.killpg(proc.pid, signal.SIGKILL)
                    proc.wait()
                    raise

def grade_remote_submissions(num_to_grade=False, cleanup=False):
    queue = CourseraQueue(args.queue, args.session, args.api_key)
    try: # Check communication with Coursera queue with a length poll.
        length = queue.length()
        if verbose:
            print('Initial Queue Length: %d' % length)
    except HTTPError:
        print('ERROR: %s' % sys.exc_info()[1], file=stderr)
        print('Error encountered when trying to contact queue.  Do you have the correct parameters?')
        print('Quitting...')
        sys.exit()

    # Continually poll queue for submissions to grade.
    number_graded = 0
    while (not num_to_grade) or (number_graded < num_to_grade):
        try:
            submission = queue.pull_submission()
        except HTTPError:
            print('ERROR: %s' % sys.exc_info()[1], file=stderr)
            submission = False # We'll just wait and try again

        # Check to make sure a submission was found.
        if not submission:
            print('No Pending Submissions, Sleeping (%ds)' % args.wait)
            time.sleep(args.wait)
            continue

        # Basic information about submission
        user_id = submission['submission_metadata']['user_id']
        part_id = submission['submission_metadata']['part_id']
        print('Submission pulled: user_id=%s, part_id=%s' % (user_id, part_id))

        # Grab submission's configuration.
        config = read_part_config(args.resources, part_id)
        if not config:
            print('Skipping submission...')
            continue
        # TODO config['solutions'] = submission['solutions']

        # Grade the submission
        student_dir = os.path.join(args.submissions, str(part_id), str(user_id))
        assert(submission['submission_encoding'] == 'base64')
        try:
            submission_code = base64.b64decode(submission['submission'].encode('utf-8')).decode('utf-8')
            results = grade_submission_code(student_dir, config, submission_code, cleanup=cleanup)
        except UnicodeDecodeError:
            results = 'Could not decode submission to unicode.'

        if not results:
            print('Failed to grade submission...')
            continue

        if hasattr(results, 'get') and 'score' in results:
            # Adjust score/feedback.
            results['score'] = adjust_score(results['score'], config)
            if verbose:
                print('Score: %.2f' % results['score'])
                print(results['feedback'])

                if results['score'] == 0:
                    # Give no feedback on test failures
                    results['feedback_after_soft_close_time'] = results['feedback_after_hard_deadline'] = ''
                    results['feedback'] = 'No feedback available for a score of 0'
        else:
            if verbose:
                print('Score: 0.00')
                print(results)
            results = {'score': 0, 'feedback': results}

        # Transform feedback into HTML
        results['feedback'] = results['feedback'].replace('\n', '<br />')
        if 'feedback_after_soft_close_time' in results:
            results['feedback_after_soft_close_time'] = results['feedback_after_soft_close_time'].replace('\n', '<br />')
        if 'feedback_after_hard_deadline' in results:
            results['feedback_after_hard_deadline'] = results['feedback_after_hard_deadline'].replace('\n', '<br />')

        # Post results
        if not queue.post_score(submission['api_state'], **results):
            print('Failed to post score...')
            continue
        else:
            number_graded += 1

def adjust_score(score, config):
    raw_score = round(score * config['grademult'], 2)
    score = min(max(raw_score, config['minimum-score']), config['maximum-score'])
    if verbose and score != raw_score:
        print('Warning: Score %.2f was out of range.  Rounding to %.2f.' % (raw_score, score))
    return float(score)

def grade_local_submissions(num_to_grade=False, cleanup=False):
    number_graded = 0
    for part_id in os.listdir(args.submissions):
        part_dir = os.path.join(args.submissions, part_id)
        if not os.path.isdir(part_dir):
            continue

        # Grab configuration for part_id.
        config = read_part_config(args.resources, part_id)
        if not config:
            continue

        print('* %s' % part_id)
        for user_id in os.listdir(part_dir):
            if num_to_grade and number_graded >= num_to_grade:
                return
            student_dir = os.path.join(args.submissions, part_id, user_id)
            if not os.path.isdir(student_dir):
                continue
            print('** %s' % user_id)

            results = grade_local_submission(student_dir, config, cleanup=cleanup)
            if not results:
                print('Failed to grade submission...')
                sys.exit() # TODO

            # Adjust score and print results.
            if not (hasattr(results, 'get') and 'score' in results):
                results = {'score': 0, 'feedback': results}
            results['score'] = adjust_score(results['score'], config)
            print('Score: %.2f' % results['score'])
            print(results['feedback'])

            number_graded += 1

if __name__ == '__main__':
    args = parse_cmd_args()
    verbose = args.verbose

    if args.pid:
        try:
            atexit.register(lambda: os.remove(args.pid))
            with open(args.pid, 'w') as f:
                f.write(str(os.getpid()))
        except:
            print('ERROR: %s' % sys.exc_info()[1], file=stderr)
            print(' Could not write pid file.', file=stderr)
            sys.exit()

    if verbose:
        print('Arguments:')
        pprint(vars(args))
        print()

    if args.local:
        grade_local_submissions(num_to_grade=args.N, cleanup=args.cleanup)
    else:
        while not args.api_key: # Prompt for API key if not already specified.
            args.api_key = getpass('Please enter your API Key: ').strip()
        if args.length:
            queue = CourseraQueue(args.queue, args.session, args.api_key)
            print('Queue Length: %d' % queue.length())
        else:
            grade_remote_submissions(num_to_grade=args.N, cleanup=args.cleanup)
