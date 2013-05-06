import subprocess
import unittest

def test_grade(file_arg):
    cmd = ['python', '../../12/tweet_sentiment_grader.py', '../../lib/AFINN-111.txt', 'smalltweets.txt', file_arg]
    return subprocess.check_output(cmd).strip()

class SentGraderTests(unittest.TestCase):

    def test_grade_success(self):
        op = test_grade('test_grade_success.txt')
        self.assertEqual(op, '1;Good Job!')

    def test_fail_parse(self):
        op = test_grade('test_fail_parse.txt')
        self.assertEqual(op ,'0;parsing error, line should be a number: -4 3')

    def test_fail_length(self):
        op = test_grade('test_fail_length.txt')
        self.assertEqual(op, '0;Expected 7 scores')

    def test_fail_value(self):
        op = test_grade('test_fail_value.txt')
        self.assertEqual(op, '0;Expected 0 for tweet #1 got: 1.0')


if __name__ == '__main__':
    unittest.main()
