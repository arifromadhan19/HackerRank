"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""

def preOrder(root):
    if root:
        print str(root.data),
        #print(str(root.data)+" ", end="") #print on python 3
        preOrder(root.left)
        preOrder(root.right)
    
    
    
    


