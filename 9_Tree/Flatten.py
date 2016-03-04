'''
Given a binary tree, flatten it to a linked list in-place.

Example :
Given

         1
        / \
       2   5
      / \   \
     3   4   6


   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
'''
class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def flatten(self, A):
    store = current = A
    while current:
        if current.left:
            prev = current.left
            while prev.right:
                prev = prev.right
            prev.right = current.right
            current.right = current.left
            current.left = None
        current = current.right
    return store

    
root = Node(1)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.right = Node(6)

print flastten(root)
