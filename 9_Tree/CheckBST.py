'''
Given a binary tree, check whether it’s a binary search tree or not.
Again, no solution cell, just worry about your code making sense logically. Hint: Think about tree traversals.
'''


tree_vals = []

def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        tree_vals.append(tree.getRootVal())
        inorder(tree.getRightChild())
        
def sort_check(tree_vals):
    return tree_vals == sorted(tree_vals)

inorder(tree)
sort_check(tree_vals)



'''
'''
class Node:
    def __init__(self, k, val):
        self.key = k
        self.value = val
        self.left = None
        self.right = None

def tree_max(node):
    if not node:
        return float("-inf")
    maxleft  = tree_max(node.left)
    maxright = tree_max(node.right)
    return max(node.key, maxleft, maxright)

def tree_min(node):
    if not node:
        return float("inf")
    minleft  = tree_min(node.left)
    minright = tree_min(node.right)
    return min(node.key, minleft, minright)

def verify(node):
    if not node:
        return True
    if (tree_max(node.left) <= node.key <= tree_min(node.right) and
        verify(node.left) and verify(node.right)):
        return True
    else:
        return False
