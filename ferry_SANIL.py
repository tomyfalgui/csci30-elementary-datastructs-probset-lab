import math
import os
import random
import re
import sys

def ferryLoading(l,m):
    ferryLength = l*100
    ferryLoad = 0
    carLengthsLeft = []
    carLengthsRight = []
    ferryLocation = "left"
    ferryCount = 0
    c1 = 0
    c2 = 0

    while m > 0:
        inp = input()
        carInput = inp.split(" ")
        if carInput[1] == "left":
            carLengthsLeft.append(int(carInput[0]))
        elif carInput[1] == "right":
            carLengthsRight.append(int(carInput[0]))
        m = m-1

    while (len(carLengthsLeft) != 0) or (len(carLengthsRight) != 0):
        if (len(carLengthsLeft) != 0) and (ferryLocation == "left"):
            while (ferryLoad <= ferryLength) and (len(carLengthsLeft) != 0):
                if ferryLoad + carLengthsLeft[0] <= ferryLength:
                    ferryLoad = ferryLoad + carLengthsLeft.pop(0)
                else:
                    break
            ferryLoad = 0
            ferryLocation = "right"
            ferryCount = ferryCount + 1
        elif (len(carLengthsRight) != 0) and (ferryLocation == "right"):
            while ferryLoad <= ferryLength and (len(carLengthsRight) != 0):
                if ferryLoad + carLengthsRight[0] <= ferryLength:
                    ferryLoad = ferryLoad + carLengthsRight.pop(0)
                else:
                    break
            ferryLoad = 0
            ferryLocation = "left"
            ferryCount = ferryCount + 1
        elif (len(carLengthsLeft) == 0) and (ferryLocation == "left") and (len(carLengthsRight) != 0):
            ferryLocation = "right"
            ferryCount = ferryCount + 1
        elif (len(carLengthsRight) == 0) and (ferryLocation == "right") and (len(carLengthsLeft) != 0):
            ferryLocation = "left"
            ferryCount = ferryCount + 1

    print(ferryCount)


def main (n):
    while n > 0:
        inp = input()
        ferryInput = inp.split(" ")
        ferryLoading(int(ferryInput[0]),int(ferryInput[1]))
        n = n-1

main(int(input()))
