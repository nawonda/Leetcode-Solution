'''
Given a singly linked list, write a function which takes in the first node in a singly linked list and returns a boolean indicating if the linked list contains a "cycle".
A cycle is when a node's next point actually points back to a previous node in the list. This is also sometimes known as a circularly linked list.
You've been given the Linked List Node class code:
'''

class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None
        
    def cycle_check(node):

    # Begin both markers at the first node
    marker1 = node
    marker2 = node

    # Go until end of list
    while marker2 != None and marker2.nextnode != None:
        
        # Note
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        # Check if the markers have matched
        if marker2 == marker1:
            return True

    # Case where marker ahead reaches the end of the list
    return False