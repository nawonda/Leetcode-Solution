'''
Problem
Given an array of integers (positive and negative) find the largest continuous sum.
A = [1,2,-1,3,4,10,10,-10,-1]
'''

def LCS(A):
    if max(A)<0:
        return max(A)
    
    L = M = 0
    
    for e in A:
        if L + e <= 0:            
            L = 0
        else:
            L += e
            M = max(M,L)
    return M

A = [1,2,-1,3,4,10,10,-10,-1]
print LCS(A)

            