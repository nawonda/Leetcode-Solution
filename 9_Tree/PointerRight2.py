'''
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root:
            p = root; q = None; nextNode = None
            while p:
                if p.left:
                    if q: q.next = p.left
                    q = p.left
                    if nextNode == None: nextNode = q
                if p.right:
                    if q: q.next = p.right
                    q = p.right
                    if nextNode == None: nextNode = q
                p = p.next
            self.connect(nextNode)
