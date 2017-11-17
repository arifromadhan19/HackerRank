"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root , s):
    current = root
    result = []
    index = 0
    while index < len(s):
        while not (current.left is None and current.right is None):
            if int(s[index]) > 0: current = current.right 
            if int(s[index]) <= 0: current = current.left 
            index += 1
        result.append(current.data)
        current=root
    print(''.join(result))
    
        