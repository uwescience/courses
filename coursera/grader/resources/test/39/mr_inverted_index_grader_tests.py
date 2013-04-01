import subprocess
import unittest

def test_grade(file_arg):
    cmd = ['python', '../../39/mr_inverted_index_grader.py', '../../39/test_success.txt', file_arg]
    return subprocess.check_output(cmd).strip()

class SentGraderTests(unittest.TestCase):

    def test_success(self):
        op = test_grade('test_success.txt')
        self.assertEqual(op, '1;Good Job!')

    def test_fail_parse(self):
        op = test_grade('test_fail_parse.txt')
        self.assertEqual(op, '0;Parse error: [ "jawbone",')

    def test_fail_incorrect_list(self):
        op = test_grade('test_fail_incorrect_list.txt')
        self.assertEqual(op, '0;Value mismatch for fawn. Expected: shakespeare-caesar.txt,whitman-leaves.txt Got: shakespeare-caesar.txt')

    def test_fail_missing_key(self):
        op = test_grade('test_fail_missing_key.txt')
        self.assertEqual(op, '0;Missing word: fawn')


if __name__ == '__main__':
    unittest.main()
