#!/bin/python3

import sys
import re

s = input().strip()
word = filter(None, re.split("([A-Z][^A-Z]*)", s))
count = 0
for i in word:
    count = count+1
print(count)
