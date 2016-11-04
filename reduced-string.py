#!/bin/python3

# www.hackerrank.com/challenges/reduced-string

string = input().strip()
charList = list(string)
double = True
while double:
    double = False
    i = 0
    while (i < len(charList) - 1):
        if charList[i] == charList[i + 1]:
            double = True
            charList.pop(i)
            charList.pop(i)
        else:
            i += 1
if len(charList) == 0:
    print("Empty String")
else:
    print(''.join(charList))