import sys

sys.path.append('../../../lib')
import grade_helper

def main():
    input_file_handle = open(sys.argv[1])
    soln = {'a' : 1}
    stdn = grade_helper.parse_str_float_lines(input_file_handle)
    grade_helper.check_terms(stdn, soln)

if __name__ == '__main__':
    main()
