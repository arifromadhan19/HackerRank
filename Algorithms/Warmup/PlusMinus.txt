#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
a=0;b=0;c=0
for i in range(len(arr)):
    a += 1 if arr[i]>0 else 0
    b += 1 if arr[i]<0 else 0
    c += 1 if arr[i]== 0 else 0

print ("{0:6f}".format(float(a)/n))
print ("{0:6f}".format(float(b)/n))
print ("{0:6f}".format(float(c)/n))