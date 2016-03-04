'''
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
'''


#for 
#add c into left
#once over s remove from the left if left is still >= s 

def subarray(A,s):    
    left = []
    for i,c in enumerate(A):
        left.append(c)
        if sum(left) >= s:
            temp_left = left
            for j in range(1,len(left)):            
                if sum(left[j:]) >= s:                    
                    temp_left = left[j:]   
                else:                
                    break
            left = temp_left                            
                    
    return len(left)


A = [2,3,1,2,4,3]

print subarray(A,7)
            
    