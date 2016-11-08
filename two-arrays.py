#!/bin/python3

# www.hackerrank.com/challenges/two-arrays

def twoArrays(A, B, n, k):
    A.sort()
    B.sort(reverse=True)
    for i in range(n):
        if A[i] + B[i] < k:
            return 'NO'
    return 'YES'

q = int(input())
results = []
for _ in range(q):
    n, k = map(int, input().strip().split(' '))
    A = [int(x) for x in input().strip().split(' ')]
    B = [int(x) for x in input().strip().split(' ')]
    results.append(twoArrays(A, B, n, k))
for result in results:
    print(result)