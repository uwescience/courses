import sys
import os
sys.path.append(os.getcwd() + '/src')
import hw

def main():
    score = 0
    feedback = 'you\'re awesome!!!'
    if hw.getval() == 1:
        score = 1
    print str(score) + ';' + feedback 

main()
