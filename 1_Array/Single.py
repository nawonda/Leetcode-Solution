'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''

class Solution:
    def singleNumber_1(self,A):        
        B = set()
        for i,c in enumerate(A):
            if c in B:
                B.remove(c)
            else:
                B.add(c)
        return B
    
    #use XOR, 1001^1100 = 0101 
    def singleNumber_2(self, A):
        ret = A[0]
        for i in range(1,len(A)):
            ret ^= A[i]
        return ret