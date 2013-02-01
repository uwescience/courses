import sys
import os

srcdir = os.getcwd() + '/src'
sys.path.append(srcdir)

import hw

def main():
    outdir = os.getcwd() + '/out'
    testlog = open(outdir + '/tests.log', 'w+')

    score = 0
    feedback = 'you\'re awesome!!!'

    if not hasattr(hw, 'query'):
        feedback = 'query undefined' 
    elif hw.query():
        score = 1

    print(str(score) + ';' + feedback, file=testlog)
    testlog.close()

main()
