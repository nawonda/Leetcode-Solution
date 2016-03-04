'''
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
'''

def sort_color(A):

    #for
    #0 to the left, 2 to the right, 1 don't move
    # use two pointer
    
    i = left_index = 0
    right_index = len(A)-1

    while left_index <= i <= right_index:
        if A[i] == 0:            
            A[i],A[left_index] = A[left_index],A[i]
            i += 1
            left_index += 1
        elif A[i] == 2:
            A[i],A[right_index] = A[right_index],A[i]
            right_index -= 1
        else:
            i += 1
    return A

#A = [2,1,1,0,0,1]
#A = [0,1,2,2,0,1]
#A = [1,1,1,1,1,1]
A = [0,0,0,1,1,0,2,1,1,2,2]
print sort_color(A)