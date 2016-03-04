'''
Write a function to reverse a Linked List in place. The function will take in the head of the list as input and return the new head of the list.
You are given the example Linked List Node class:
'''

class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None
    
    def reverse(head):

    current = head
    previous = None
    nextnode = None

    while current:

        #set node from previous setup
        nextnode = current.nextnode
        current.nextnode = previous
        
        #set for the next iteration
        previous = current
        current = nextnode

    return previous     