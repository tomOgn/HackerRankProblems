#!/bin/python3

# www.hackerrank.com/challenges/new-year-chaos

import sys

def getMinBribes(q):
    bribes = 0
    for i in range(len(q)):
        if q[i] - i > 3:
            return "Too chaotic"
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1
                
    return bribes

t = int(input().strip())
results = []
for _ in range(t):
    _ = input()
    q = [int(x) for x in input().strip().split(' ')]
    results.append(getMinBribes(q))
for result in results:
    print(result)