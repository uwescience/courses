import sys

sys.path.append('../../../lib')
import grade_helper

def main():
    input_file_handle = open(sys.argv[1])
    grade_helper.parse_top_ten_file(input_file_handle)

if __name__ == '__main__':
    main()
