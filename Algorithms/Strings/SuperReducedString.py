#!/bin/python3

import sys

def super_reduced_string(s):
    ar=[]
    for i in range(len(s)):
        if (not ar) or (s[i] != ar[-1]):
            ar += s[i]
        else:
            l = ar.pop()

    if ar:
        return ''.join(ar)
    else:
        return "Empty String"

s = input().strip()
result = super_reduced_string(s)
print(result)
