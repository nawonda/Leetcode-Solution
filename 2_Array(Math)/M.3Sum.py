'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

For example, given array S = {-1 0 1 2 -1 -4},

(-1, 0, 1)
(-1, -1, 2)
'''

def tree_sum(A):
    if len(A) < 3:
        return
    
    A.sort()
    solution = set()
    
    for i in range(len(A)-2):
        j = i+1
        k = len(A)-1
        
        while j < k:
            if A[j]+A[k]+A[i] == 0:
                solution.add((A[i],A[j],A[k]))
                j += 1
                k -= 1
            if A[j]+A[k]+A[i] < 0:
                j += 1
            
            if A[j]+A[k]+A[i] > 0:
                k -= 1
                
    return solution

num = [-1, 0, 1, 2, -1, -4]
print tree_sum(num)


