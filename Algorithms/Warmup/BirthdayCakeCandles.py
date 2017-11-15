#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    i=0
    max_v=max(ar)
    for d_i in range(n):
        if ar[d_i] == max_v:
            i = i+1
    return i

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
