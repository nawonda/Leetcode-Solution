'''
Remove Duplicates from Sorted Array I
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
For example,
Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2].
'''

#hint: two pointers

def remove_duplicates1(A):
    #pointer1 => loop
    #pointer2 => end of the valid array
    end = 1
    value = A[0]
    for i in range(1,len(A)):
        if A[i] != value:
            value = A[i]
            A[i],A[end] = A[end],A[i]
            end += 1    
            
    return end
            
A = [1,1,2,3,3,4,4,4,5,6]            
print remove_duplicates(A)



'''
Remove Duplicates from Sorted Array II
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?
For example,
Given sorted array A = [1,1,1,2,2,3],
Your function should return length = 5, and A is now [1,1,2,2,3].
'''

def remove_duplicates2(A):
    if len(A) < 3:
        return A
    end = 1
    for i in range(1,len(A)):
        if A[i] != A[end-1]:#since it allows duplicates to 2
            end += 1
            A[i],A[end] = A[end],A[i]
    return A        
    
A = [1,1,1,1,1,2,2,2,2,2,3]        
print remove_duplicates2(A)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    