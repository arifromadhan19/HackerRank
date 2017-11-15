#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):
    j1 = v1 - x1
    j2 = v2 - x2
    j_1 = 0
    j_2 = 0
    if v1 <= v2:
        return "NO"
    else:
        if ((x2 - x1) % (v1 - v2) == 0):
            return "YES"
        else:
            return "NO"
    

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
