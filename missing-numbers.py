# www.hackerrank.com/challenges/missing-numbers

import collections

def missingNumbers(a, b):
    counterA = collections.Counter(a)
    counterB = collections.Counter(b)
    return ' '.join(str(x) for x in sorted(counterA - counterB))

n1 = int(input());
a1 = map(int, input().strip().split(' '))
n2 = int(input());
a2 = map(int, input().strip().split(' '))
print(missingNumbers(a1, a2) if (n1 > n2) else missingNumbers(a2, a1))