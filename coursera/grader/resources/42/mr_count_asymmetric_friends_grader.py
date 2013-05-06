import sys
sys.path.append('../../../resources/lib')
import grade_helper
import json

def gen_dict(stdn_file, graded):
    result = []
    for record_str in stdn_file:
        try:
            record = json.loads(record_str)
            result.append(record)
        except:
            if graded:
                grade_helper.fail('Parse error: ' + record_str)
    return sorted(result)

def grade(soln, stdn):
    for soln_record, stdn_record  in zip(soln, stdn):
        if soln_record != stdn_record:
            grade_helper.fail('Record mismatch, expected: ' + str(soln_record) + ' got: ' + str(stdn_record))

    grade_helper.success()

def main():
    soln_file = open(sys.argv[1])
    soln_set = gen_dict(soln_file, False)
    stdn_file = open(sys.argv[2])
    stdn_set = gen_dict(stdn_file, True)
    grade(soln_set, stdn_set)

if __name__ == '__main__':
    main()
