"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
    temp = head
    if position == 0:
        return temp.next
    current_position = 1
    while position - current_position > 0:
        head = head.next
        position = position -1
    head.next = head.next.next
    return temp
  
  
  
  
  
