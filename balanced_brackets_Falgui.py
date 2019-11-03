#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []

    for b in s:
        if b == '{' or b == '[' or b == '(':
            stack.append(b)
        elif b == '}':
            if len(stack) == 0 or stack.pop() != '{':
                return "NO"
        elif b == ']':
            if len(stack) == 0 or stack.pop() != '[':
                return "NO"
        elif b == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return "NO"
        

    return "YES" if len(stack) == 0 else "NO"


        

    print(stack)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

# https://www.hackerrank.com/challenges/balanced-brackets/submissions/code/129407104