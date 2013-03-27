import subprocess
import unittest

def test_grade(file_arg):
    cmd = ['python', '../../17/freq_grader.py', 'smalltweets.txt', file_arg]
    return subprocess.check_output(cmd).strip()

class SentGraderTests(unittest.TestCase):

    def test_grade_success(self):
        op = test_grade('test_grade_success.txt')
        self.assertEqual(op, '1;Good Job!')

    def test_grade_fail_max_mid(self):
        op = test_grade('test_grade_fail_max_mid.txt')
        self.assertEqual(op, '0;todo(0.0198675496689) has a greater frequency than me(0.0129801324503)')

    def test_grade_fail_mid_min(self):
        op = test_grade('test_grade_fail_mid_min.txt')
        self.assertEqual(op, '0;dijo(0.0266225165563) has a greater frequency than todo(0.0198675496689)')

if __name__ == '__main__':
    unittest.main()
