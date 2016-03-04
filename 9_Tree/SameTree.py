'''
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
'''

class Solution:
    def detectTree(self,A,B):
        if A == None and B == None:
            return True
        if A == None or B == None:
            return False
        
        return int(A.val == B.val and detectTree(self,A.left,B.left) and detectTree(self,A.right,B.right))
        
    