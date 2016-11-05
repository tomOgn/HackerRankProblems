#!/bin/python3

# https://www.hackerrank.com/challenges/python-mutations

s = input()
l = input().strip().split(' ')
i, c = int(l[0]), l[1]
print(s[0 : i] + c + s[i + 1 :])