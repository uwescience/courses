import subprocess
import unittest

def test_grade(file_arg):
    cmd = ['python', '../../40/mr_relational_join_grader.py', file_arg]
    return subprocess.check_output(cmd).strip()

class SentGraderTests(unittest.TestCase):

    def test_success(self):
        op = test_grade('test_success.txt')
        self.assertEqual(op, '1;Good Job!')

    def test_fail(self):
        op = test_grade('test_fail.txt')
        self.assertEqual(op, '0;')

if __name__ == '__main__':
    unittest.main()
