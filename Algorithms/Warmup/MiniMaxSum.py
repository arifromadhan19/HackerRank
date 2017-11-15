#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))
i= 0
result = []
for a in range(len(arr)):
    sum_result = sum(arr) - arr[i]
    result.append(sum_result)
    i =i+1
max_v = max(result)
min_v = min(result)
print (min_v, max_v)