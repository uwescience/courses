import subprocess
import unittest

def test_grade(file_arg):
    cmd = ['python', '../../40/mr_relational_join_grader.py', '../../40/test_success.txt', file_arg]
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
        self.assertEqual(op, '0;Parse error: ["35236", "128398", "O", "59650.64", "1997-06-08", "2-HIGH", "Clerk#000000705","0", " the accounts. sometimes even reques", "35236", "2951", "7952", "1", "31","57472.45", "0.03", "0.07", "N", "O", "1997-09-22", "1997-09-01", "1997-10-16","NONE", "MAIL", "eans. slyly final ideas after"')

    def test_fail_missing_value(self):
        op = test_grade('test_fail_missing_value.txt')
        self.assertNotEqual(op, '1;Good Job!')

if __name__ == '__main__':
    unittest.main()
