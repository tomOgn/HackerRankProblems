#!/bin/python3

# https://www.hackerrank.com/challenges/no-idea

def getHappiness(array, A, B):
    happiness = 0
    for item in array:
        if item in A:
            happiness += 1
        elif item in B:
            happiness -= 1
    return happiness

m, n = map(int, input().strip().split(' '))
array = [int(x) for x in input().strip().split(' ')]
A = set([int(x) for x in input().strip().split(' ')])
B = set([int(x) for x in input().strip().split(' ')])
print(getHappiness(array, A, B))