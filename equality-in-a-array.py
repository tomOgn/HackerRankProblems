#!/bin/python3

# www.hackerrank.com/challenges/equality-in-a-array

import sys, collections

_ = input()
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(len(a) - collections.Counter(a).most_common(1)[0][1])