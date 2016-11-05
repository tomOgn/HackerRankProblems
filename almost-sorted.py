#!/bin/python3

# https://www.hackerrank.com/challenges/almost-sorted

def firstUnordered(a):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return i

def isSwapEnough(a):
    # Get first unordered number
    u = firstUnordered(a)
    
    # Swap 'u' with the number positioned where 'u' would be if 'a' was ordered
    swapped = False
    for i in range(len(a) - 1):
        if a[u] < a[i + 1]:
            a[u], a[i] = a[i], a[u]
            swapped = i
            break
    # Separate case: the position was at the end of 'a'
    if not swapped:
        a[u], a[len(a) - 1] = a[len(a) - 1], a[u]
        swapped = len(a) - 1
    
    # If now 'a' is sorted than answer yes
    if isSorted(a):
        return ['yes', 'swap %d %d' % (u + 1, swapped + 1)]
    
    return False
    
def isReverseEnough(a):
    # Get first unordered number
    u = []
    i = firstUnordered(a)
    u.append(i)
    i += 1
    
    # Get all successive numbers as long as they are in decreasing order
    while i < len(a) - 1 and a[i] > a[i + 1]:
        u.append(i)
        i += 1
        
    # Get all successive numbers as long as they are lesser than u[0]
    while i < len(a) and a[i] < a[u[0]]:
        u.append(i)
        i += 1
        
    # Make a new list with all numbers before 'u', plus all numbers in 'u' in reverse order, 
    # plus all numbers after 'u'. If the new list is ordered than answer yes.
    if isSorted(a[ : u[0]] + a[u[0] : u[len(u) - 1] + 1][::-1] + a[u[len(u) - 1] + 1 : ]):
        return ['yes', 'reverse %d %d' % (u[0] + 1, u[len(u) - 1] + 1)]
    return ['no']
        
def isSorted(a):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True

def almostSorted(a):
    if isSorted(a):
        return ['yes']
    output = isSwapEnough(list(a))
    if not output:
        output = isReverseEnough(a)
    for line in output:
        print(line)
    
_ = int(input())
a = [int(x) for x in input().strip().split(' ')]
almostSorted(a)