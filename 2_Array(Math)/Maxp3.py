'''
Given an array of integers, return the highest product possible by multiplying 3 numbers from the array
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        if len(A) < 3:
            return 0
        A = sorted(A)
        p = A[-1]*A[-2]*A[-3]
        n = A[-1]*A[0]*A[1]
        return max(p,n)