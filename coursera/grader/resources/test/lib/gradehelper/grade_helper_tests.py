import subprocess
import unittest

def get_output_py_script(args):
    cmd = ['python']
    cmd.extend(args)
    return subprocess.check_output(cmd).strip()

def test_parse_str_float_lines(file_arg):
    return get_output_py_script(['test_parse_str_float_lines.py', file_arg])

def test_check_terms(file_arg):
    return get_output_py_script(['test_check_terms.py', file_arg])

def test_parse_state(file_arg):
    return get_output_py_script(['test_parse_state.py', file_arg])

def test_parse_top_ten_file(file_arg):
    return get_output_py_script(['test_parse_top_ten_file.py', file_arg])

class GradeHelperTests(unittest.TestCase):

    def test_parse_str_float_lines_success(self):
        op = test_parse_str_float_lines('test_parse_str_float_lines_success.txt')
        self.assertEqual(op, '')

    def test_parse_str_float_lines_fail_format(self):
        op = test_parse_str_float_lines('test_parse_str_float_lines_fail_format.txt')
        self.assertEqual(op, '0;Formatting error: a 1 1')

    def test_parse_str_float_lines_fail_float(self):
        op = test_parse_str_float_lines('test_parse_str_float_lines_fail_float.txt')
        self.assertEqual(op, '0;value is not parseable as float: a b')

    def test_check_terms_fail(self):
        op = test_check_terms('test_check_terms_fail.txt')
        self.assertEqual(op, '0;a has no computed value')

    def test_check_terms_success(self):
        op = test_check_terms('test_check_terms_success.txt')
        self.assertEqual(op, '')

    def test_parse_state_success(self):
        op = test_parse_state('test_parse_state_success.txt')
        self.assertEqual(op, '')

    def test_parse_state_fail_length(self):
        op = test_parse_state('test_parse_state_fail_lines.txt')
        self.assertEqual(op, '0;Input contains multiple lines')

    def test_parse_state_fail_abbrev(self):
        op = test_parse_state('test_parse_state_fail_abbrev.txt')
        self.assertEqual(op, '0;CAT is not a 2 character state abbreviation')

    def test_parse_top_ten_file_success(self):
        op = test_parse_top_ten_file('test_parse_top_ten_file_success.txt')
        self.assertEqual(op, '')

    def test_parse_top_ten_file_fail_format(self):
        op = test_parse_top_ten_file('test_parse_top_ten_file_fail_format.txt')
        self.assertEqual(op, '0;Formatting error: a 1 1')

    def test_parse_top_ten_file_fail_int(self):
        op = test_parse_top_ten_file('test_parse_top_ten_file_fail_int.txt')
        self.assertEqual(op, '0;Value is not an integer: a b')

    def test_parse_top_ten_file_fail_length(self):
        op = test_parse_top_ten_file('test_parse_top_ten_file_fail_length.txt')
        self.assertEqual(op, '0;There are not exactly ten values in your solution.')
    
if __name__ == '__main__':
    unittest.main()
