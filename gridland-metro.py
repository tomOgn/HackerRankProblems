#!/bin/python3

# www.hackerrank.com/challenges/gridland-metro

def isSubset(a, b):
    return (b[0] <= a[0] and b[1] >= a[1]) or (a[0] <= b[0] and a[1] >= b[1])

def isOverlap(a, b):
    return (b[0] < a[0] and a[0] <= b[1] < a[1]) or (a[0] < b[0] and b[0] <= a[1] < b[1])

def union(a, b):
    return [min(a[0], b[0]), max(a[1], b[1])]

n, m, k = map(int, input().strip().split(' '))
trains = {}
for _ in range(k):
    r, c1, c2 = map(int, input().strip().split(' '))
    trains.setdefault(r, [])
    row = trains[r]
    newTrain = [c1, c2]
    overlapping = False
    for i in range(len(row)):
        if isOverlap(row[i], newTrain) or isSubset(row[i], newTrain):
            row[i] = union(row[i], newTrain)          
            overlapping = True
            break
    if not overlapping:
        row.append(newTrain)
t = 0
for _, row in trains.items():
    for train in row:
        t += train[1] - train[0] + 1
print(n * m - t)