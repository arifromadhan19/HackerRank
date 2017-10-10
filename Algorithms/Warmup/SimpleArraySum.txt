#!/bin/python3

import sys

def simpleArraySum(n, ar):
    result = 0
    for r in ar:
        result +=r
    return result

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)
