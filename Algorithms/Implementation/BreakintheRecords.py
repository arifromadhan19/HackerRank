#!/bin/python3

import sys

def getRecord(s):
    max_score, min_score = s[0],s[0]
    max_count = 0
    min_count = 0
    for score in s:
        if score > max_score:
            max_score = score
            max_count = max_count + 1
        elif score < min_score:
            min_score = score
            min_count = min_count + 1
    return max_count, min_count 

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
