#!/bin/python3

# www.hackerrank.com/challenges/between-two-sets

import sys

def isFactor(x, a):
    for element in a:
        if element % x != 0:
            return False
    return True

def hasFactors(x, a):
    for element in a:
        if x % element != 0:
            return False
    return True

n, m = [int(x) for x in input().strip().split(' ')]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(b_temp) for b_temp in input().strip().split(' ')]

count = 0
for x in range(max(a), min(b) + 1):
    if isFactor(x, b) and hasFactors(x, a):
        count += 1
        
print(count)