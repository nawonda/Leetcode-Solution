'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4

'''

def maximal_square(A):
    max_count = 1
    for i in range(len(A)):
        
        for j in range(len(A[0])):
    
            if A[i][j] == 1:
                temp_count = check(A,i,j,1)
                max_count = max(temp_count,max_count)
    
    return max_count

def check(A,i,j,count):
    
    if i+1 < len(A) and j+1 < len(A[0]):
        if A[i+1][j] == A[i][j+1] == A[i+1][j+1] == 1:
            count +=1
            count = min(check(A,i+1,j,count),check(A,i,j+1,count),check(A,i+1,j+1,count))

    return count


A = [
[1,0,0,0,0],
[1,0,0,1,1],
[1,0,1,1,1],
[1,0,1,1,1]
]   

print maximal_square(A)