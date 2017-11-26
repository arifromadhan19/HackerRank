#!/bin/python3

import sys

def solve(grades):
    gr =[]
    for i in range(len(grades)):
        cek = ((5 * int(grades[i] / 5)) + 5) - grades[i]
        if grades[i] < 38:
            gr.append(grades[i])
        else:
            if cek < 3:
                h = grades[i] + 2
                gr.append(grades[i] + 2)
            else:
                h = grades[i]
                gr.append(grades[i])
    return gr

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))


============================================
#!/bin/python2
import sys
n = int(raw_input().strip())
for a0 in xrange(n):
    grade = int(raw_input().strip())
    if grade < 38:
        print (grade)
        continue
    difference = 5 - (grade % 5)
    if difference < 3:
        print (grade+difference)
    else:
        print (grade)
