#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    shifting = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    new_array = [0] * len(a)

    for idx in range(len(a)):
        new_array[idx - shifting] = a[idx]

    print(*new_array, sep=" ")


#https://www.hackerrank.com/challenges/array-left-rotation/submissions/code/129390591
    
