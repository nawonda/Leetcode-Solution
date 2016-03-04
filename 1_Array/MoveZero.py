'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

def moveNoneZeros2(A):
    n = len(A)
    count = 0
    for i in range(n):
        if(A[i] != 0):            
            A[count] = A[i]
            count += 1
    
    for i in range(count,n):
        A[i] = 0
    
    return A
    
A = [0, 1, 0, 3, 12]        
print moveNoneZeros2(A)    
    
    
    
    
    
    
    
        
        
        
        
        
    
