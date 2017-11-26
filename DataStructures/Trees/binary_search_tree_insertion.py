"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def insert(r,val):
    if r == None:
        r = Node('')
        r.data =val
    else:
        if val < r.data:
            if r.left:
                insert(r.left,val)
            else:
                r.left =Node('')
                r.left.data = val       
        else:
            if r.right:
                insert(r.right,val)
            else:
                r.right =Node('')
                r.right.data = val
    return r
 
             
        
        
