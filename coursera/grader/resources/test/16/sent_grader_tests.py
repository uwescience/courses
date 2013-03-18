import subprocess
import unittest

def test_grade(file_arg):
    cmd = ['python', '../../16/sent_grader.py', '../../lib/AFINN-111.txt', 'smalltweets.txt', file_arg]
    return subprocess.check_output(cmd).strip()

class SentGraderTests(unittest.TestCase):

    def test_grade_success(self):
        op = test_grade('test_grade_success.txt')
        self.assertEqual(op, '1;Good Job!')

    def test_grade_fail_max_mid(self):
        op = test_grade('test_grade_fail_max_mid.txt')
        self.assertEqual(op, '0;love(2.0) has a greater sentiment score than for(1.0)')

    def test_grade_fail_mid_min(self):
        op = test_grade('test_grade_fail_mid_min.txt')
        self.assertEqual(op, '0;Alto(1.0) has a greater sentiment score than love(0.0)')

if __name__ == '__main__':
    unittest.main()
