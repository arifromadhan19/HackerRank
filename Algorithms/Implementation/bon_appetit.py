#!/bin/python

import sys

def bonAppetit(n, k, b, ar):
    total = sum(ar) - ar[k]
    half = total/2
    if (b-half) == 0:
        return "Bon Appetit"
    else:
        sisa = b-half
        return int(sisa)

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
b = int(raw_input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
