#!/bin/python3

# www.hackerrank.com/challenges/coin-change

def coinChangeR(array, index, partialSum, totalSum, count):
    for j in range(index, len(array)):
        print("j = ", j, " index = ", index, " partial = ", partialSum, " count = ", count)
        if partialSum + array[j] < totalSum:
            count += coinChangeR(array, index, partialSum + array[j], totalSum, count)
        elif partialSum + array[j] == totalSum:
            return 1
        else:
            return 0
    return count
n, m = map(int, input().strip().split(' '))
c = [int(x) for x in input().strip().split(' ')]
print(coinChangeR(c, 0, 0, n, 0))