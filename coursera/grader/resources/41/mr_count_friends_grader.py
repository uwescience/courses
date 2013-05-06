import sys
sys.path.append('../../../resources/lib')
import grade_helper
import json

def gen_dict(stdn_file, graded):
    result = {}
    for pair in stdn_file:
        try:
            pair_dict = json.loads(unicode(pair, encoding='latin-1'))
            result.update(pair_dict)
        except:
            if graded:
                grade_helper.fail('Parse error: ' + pair)
    return result

def grade(soln, stdn):
    for key in soln:
        if key not in stdn:
            grade_helper.fail('Missing person: ' + key)
        elif soln[key] != stdn[key]:
            grade_helper.fail('Value mismatch for ' + key + '. Expected: ' + str(soln[key]) + ' Got: ' + str(stdn[key]))

    grade_helper.success()

def main():
    soln_file = open(sys.argv[1])
    soln_dict = gen_dict(soln_file, False)
    stdn_file = open(sys.argv[2])
    stdn_dict = gen_dict(stdn_file, True)
    grade(soln_dict, stdn_dict)

if __name__ == '__main__':
    main()
