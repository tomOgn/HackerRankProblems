#!/bin/python3

# www.hackerrank.com/challenges/simple-text-editor

def simpleTextEditor(operations):
    s = []
    history = []
    for operation in operations:
        id = int(operation[0])
        if id == 1:
            history.append(list(s))
            s += list(operation[1])
        elif id == 2:
            history.append(list(s))
            s = s[0 : len(s) - int(operation[1])]
        elif id == 3:
            print(s[int(operation[1]) - 1])
        else:
            s = history.pop()

n = int(input())
operations = []
for _ in range(n):
    operations.append([x for x in input().strip().split(' ')])
simpleTextEditor(operations)