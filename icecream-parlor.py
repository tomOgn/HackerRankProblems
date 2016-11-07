#!/bin/python3

# www.hackerrank.com/challenges/icecream-parlor

def iceCreamParlor(m, c):
    for i in range(len(c) - 1):
        for j in range(i + 1, len(c)):
            if c[i] + c[j] == m:
                return str(i + 1) + ' ' + str(j + 1)

t = int(input())
trips = []
for _ in range(t):
    m = int(input())
    _ = int(input())
    c = [int(x) for x in input().strip().split(' ')]
    trips.append((m, c))
results = []
for trip in trips:
    results.append(iceCreamParlor(trip[0], trip[1]))
for result in results:
    print(result)