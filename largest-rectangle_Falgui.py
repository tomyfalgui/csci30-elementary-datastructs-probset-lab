#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    stack = [-1]
    max_area = 1

    for idx in range(len(h)):
        while stack[-1] != -1 and h[stack[-1]] >= h[idx]:
            last_el_index = stack.pop()
            max_area = max(max_area, h[last_el_index] * (idx - stack[-1] - 1))

        stack.append(idx)

    
    while stack[-1] != -1:
        last_el_index = stack.pop()
        max_area = max(max_area, h[last_el_index] * (len(h) - stack[-1] - 1))

    return max_area




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()

# https://www.hackerrank.com/challenges/largest-rectangle/submissions/code/129413999