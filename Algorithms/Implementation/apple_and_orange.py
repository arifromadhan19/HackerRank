#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

h_apple = 0
h_orange = 0
for i in range(len(apple)):
    position = a + apple[i]
    if (position >= s) and (position <= t):
        h_apple +=1
print(h_apple)

for i in orange:
    position = b + i
    if (position >= s) and (position <= t):
        h_orange += 1
print(h_orange)