import subprocess
import unittest

def test_grade(file_arg):
    cmd = ['python', '../../44/mr_matrix_multiply_grader.py', '../../44/test_success.txt', file_arg]
    return subprocess.check_output(cmd).strip()

class SentGraderTests(unittest.TestCase):

    def test_success(self):
        op = test_grade('test_success.txt')
        self.assertEqual(op, '1;Good Job!')

    def test_success_out_of_order(self):
        op = test_grade('test_success_out_of_order.txt')
        self.assertEqual(op, '1;Good Job!')

    def test_fail_parse(self):
        op = test_grade('test_fail_parse.txt')
        self.assertEqual(op, '0;Parse error: [7, 3, 20375')

    def test_fail_missing_value(self):
        op = test_grade('test_fail_missing_value.txt')
        self.assertNotEqual(op, '1;Good Job!')

if __name__ == '__main__':
    unittest.main()
