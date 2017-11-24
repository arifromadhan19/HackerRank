"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
    if not position == 0:
        current = head
        current_position = 1
        while(position - current_position>0):
            current = current.next
            current_position+=1
        if current.next is None:
            current.next = Node(data,None)
            return head
        else:
            prev = current.next
            current.next = Node(data,prev)
            return head
    else:
        return Node(data,head)
  
  
  
  
  
  
  
  
  
  
