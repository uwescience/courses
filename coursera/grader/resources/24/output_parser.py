import sys
sys.path.append('../../../resources/lib')
import grade_helper
import json

def parse(output):
    for obj in output:
        try:
            json.loads(obj)
        except:
            grade_helper.fail('Parse error: ' + obj)

def main():
    output = open(sys.argv[1])
    parse(output)
    grade_helper.success()

if __name__ == '__main__':
    main()
