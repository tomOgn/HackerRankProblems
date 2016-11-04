# www.hackerrank.com/challenges/ctci-ransom-note

import collections

def ransom_note(magazine, ransom):
    collectionM = collections.Counter(magazine)
    collectionR = collections.Counter(ransom)
    return collectionM & collectionR == collectionR
   
m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if answer:
    print("Yes")
else:
    print("No")