#!/bin/python3

# www.hackerrank.com/challenges/minimum-distances

import sys

def minimumDistance(A, n):
    distance = -1
    d = {}
    for i in range(n):
        j = d.get(A[i], -1)
        if j >= 0 and (distance == -1 or distance > i - j):
            distance = i - j
        d[A[i]] = i
    return distance

n = int(input().strip())
A = [int(x) for x in input().strip().split(' ')]
print(minimumDistance(A, n))