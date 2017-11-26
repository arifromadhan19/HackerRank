"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def levelOrder(root):
    this_level = [root]
    while this_level:
        next_level = []
        for i in this_level:
            print i.data,
            if i.left: next_level.append(i.left)
            if i.right: next_level.append(i.right)
        this_level = next_level
