import sys
sys.path.append('../../../resources/lib')
import grade_helper
import json

def gen_dict(stdn_file, graded):
    result = set()
    duplicate = False
    for record_str in stdn_file:
        try:
            record = json.loads(record_str)
            if record in result and graded:
                duplicate = True
            else:
                result.add(record)
        except:
            if graded:
                grade_helper.fail('Parse error: ' + record_str)

    if duplicate:
        grade_helper.fail('Duplicate input: ' + record)

    return result

def grade(soln, stdn):
    diff = soln - stdn
    if len(diff) != 0:
        grade_helper.fail('Expected student solution to contain: ' + ','.join(diff))

    diff = stdn - soln
    if len(diff) != 0:
        grade_helper.fail('Student solution contains extraneous data: ' + ','.join(diff))

    grade_helper.success()

def main():
    soln_file = open(sys.argv[1])
    soln_set = gen_dict(soln_file, False)
    stdn_file = open(sys.argv[2])
    stdn_set = gen_dict(stdn_file, True)
    grade(soln_set, stdn_set)

if __name__ == '__main__':
    main()
