#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    for x in s:
        if x == '(':
            stack.append('(')
        elif (x== ')'):
            if(len(stack) >0 and stack[-1] == '('):
                stack.pop()
            else:
                return 'NO'
        elif x=='[':
            stack.append('[')
        elif (x==']'):
            if(len(stack) >0 and stack[-1] == '['):
                stack.pop()
            else:
                return 'NO'
        elif x == '{':
            stack.append('{')
        elif (x=='}'):
            if(len(stack) >0 and stack[-1]=='{'):
                stack.pop()
            else:
                return 'NO'
    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

#https://www.hackerrank.com/challenges/balanced-brackets/submissions/code/129389520