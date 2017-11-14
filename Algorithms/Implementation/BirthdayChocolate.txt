#!/bin/python3

import sys

def solve(n, s, d, m):
    count = 0
    for i in range(len(s)):
        if sum(s[i:i + m]) == d:
            count = count+1

    #Simple Way
    #count = sum([1 for i in range(n-m+1) if sum(s[i:i+m]) == d])

    return count

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)