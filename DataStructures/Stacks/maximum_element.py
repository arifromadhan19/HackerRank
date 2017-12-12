#FIRST WAY
###########################
n = int(input().strip())
stack = []
max_stack = [0]

for i in range(n):
    x = list(map(int, input().split()))
    if x[0]==1:
        stack.append(x[1])
        if x[1] >= max_stack[-1]:
            max_stack.append(x[1])
    elif x[0]==2:
        if stack.pop() == max_stack[-1]:
            max_stack.pop()
    else:
        print(max_stack[-1])

# SECOND WAY
###########################
class Stack:
    def __init__(self):
        self.stack = [0]
        self.max_stack = [0]

    def push(self, item):
        self.stack.append(item)
        if item >= self.max_stack[-1]:
            self.max_stack.append(item)

    def pop(self):
        if self.stack[-1] == self.max_stack[-1]:
            self.max_stack.pop()
        self.stack.pop()


s = Stack()
n = int(input().strip())
for i in range(n):
    x = list(map(int, input().split()))
    if x[0] == 1:
        s.push(int(x[1]))

    elif x[0] == 2:
        s.pop()

    else:
        print(s.max_stack[-1])


