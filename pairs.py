#!/bin/python3

# www.hackerrank.com/challenges/pairs

def pairs(a, k):
    a.sort()
    start = 0
    end = 1
    count = 0
    while start < len(a) and end < len(a):
        diff = a[end] - a[start]
        if diff == k:
            count += 1
            start += 1
            end += 1
        elif diff > k:
            start += 1
        else:
            end += 1
    return count