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

    term = 'random'

    if not hasattr(hw, 'top_ten_hash_tags'):
        feedback = 'top_ten_hash_tags undefined' 
    elif hw.top_ten_hash_tags():
        score = 1

    print(str(score) + ';' + feedback, file=testlog)
    testlog.close()

main()
