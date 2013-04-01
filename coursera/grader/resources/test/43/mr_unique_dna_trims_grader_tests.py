import subprocess
import unittest

def test_grade(file_arg):
    cmd = ['python', '../../43/mr_unique_dna_trims_grader.py', '../../43/test_success.txt', file_arg]
    return subprocess.check_output(cmd).strip()

class SentGraderTests(unittest.TestCase):

    def test_success(self):
        op = test_grade('test_success.txt')
        self.assertEqual(op, '1;Good Job!')

    def test_success_out_of_order(self):
        op = test_grade('test_success_out_of_order.txt')
        self.assertEqual(op, '1;Good Job!')

    def test_fail_missing_value(self):
        op = test_grade('test_fail_missing_value.txt')
        self.assertEqual(op, '0;Expected student solution to contain: CCCAGCCTCA')

    def test_fail_extra_value(self):
        op = test_grade('test_fail_extra_value.txt')
        self.assertEqual(op, '0;Student solution contains extraneous data: CCCAGCCTCAE')

    def test_fail_duplicate_value(self):
        op = test_grade('test_fail_duplicate_value.txt')
        self.assertEqual(op, '0;Duplicate input: GCACCAGCCC')
    
    def test_fail_parse(self):
        op = test_grade('test_fail_parse.txt')
        self.assertEqual(op, '0;Parse error: "CCCAGCCTCA')

if __name__ == '__main__':
    unittest.main()
