import subprocess
import unittest

def test_grade(file_arg):
    cmd = ['python', '../../41/mr_count_friends_grader.py', '../../41/test_success.txt', file_arg]
    return subprocess.check_output(cmd).strip()

class SentGraderTests(unittest.TestCase):

    def test_success(self):
        op = test_grade('test_success.txt')
        self.assertEqual(op, '1;Good Job!')

    def test_fail_parse(self):
        op = test_grade('test_fail_parse.txt')
        self.assertEqual(op, '0;Parse error: {"Gueulemer": 20')

    def test_fail_count(self):
        op = test_grade('test_fail_count.txt')
        self.assertEqual(op, '0;Value mismatch for Gueulemer. Expected: 20 Got: 21')

    def test_fail_missing_person(self):
        op = test_grade('test_fail_missing_person.txt')
        self.assertEqual(op, '0;Missing person: Gueulemer')

if __name__ == '__main__':
    unittest.main()
