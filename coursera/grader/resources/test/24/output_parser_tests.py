import subprocess
import unittest

def test_grade(file_arg):
    cmd = ['python', '../../24/output_parser.py', file_arg]
    return subprocess.check_output(cmd).strip()

class SentGraderTests(unittest.TestCase):

    def test_grade_success(self):
        op = test_grade('test_success.txt')
        self.assertEqual(op, '1;Good Job!')

    def test_fail_parse(self):
        op = test_grade('test_fail_parse.txt')
        self.assertEqual(op ,'0;Parse error: {"delete":{"status":{"id":244624316732436480,"user_id":234666175,"id_str":"244624316732436480","user_id_str":"234666175"}}')

if __name__ == '__main__':
    unittest.main()
