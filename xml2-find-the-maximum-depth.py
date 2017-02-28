#!/bin/python3

# https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth

import sys

maxdepth = -1
def depth(root, level):
    global maxdepth
    if level == maxdepth:
        maxdepth += 1
    for child in root:
        depth(child, level + 1)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)