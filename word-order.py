#!/bin/python3

# www.hackerrank.com/challenges/word-order

from collections import Counter

n = int(input())
counter = Counter()
words = set()
order = []
for _ in range(n):
    word = input().strip()
    counter[word] += 1
    if not word in words:
        words.add(word)
        order.append(word)
print(len(counter))
print(" ".join(str(counter[word]) for word in order))