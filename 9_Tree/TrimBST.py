'''
Given the root of a binary search tree and 2 numbers min and max, trim the tree such that all the numbers in the new tree are between min and max (inclusive). The resulting tree should still be a valid binary search tree. So, if we get this tree as input:
'''

def trim(root,lower,upper):
    #base
    if not root:
        return
    
    #recursive
    root.left = trim(root.left,lower,upper)
    root.right = trim(root.right,lower,upper)
    
    #assume root.left and root.right are all valid
    #let's consider only root itself
    if root.val < lower:
        return root.right
    elif root.val > upper:
        return root.left
    else:
        return root