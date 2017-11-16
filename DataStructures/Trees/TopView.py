"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def topView(root, count=0):
    if root != None:
        if count <= 0:
            topView(root.left, -1)
        print(root.data),
        if count >= 0:
            topView(root.right, 1)
             
    

    

