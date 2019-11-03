#!/bin/python3
from __future__ import print_function
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

#n = umber of integers
#d = number of rotations
#a = array of integers
b = len(a)-1
while d > 0:
    store=a[0]
    a.pop(0)
    a.append(store)
    d=d-1

print (*a, sep= ' ')

#https://www.hackerrank.com/challenges/array-left-rotation/submissions/code/129382453