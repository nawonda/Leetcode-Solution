'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''

def two_sum(num,target):
    
    processed = {}
    for i in range(0, len(num)):
        if target-num[i] in processed:
            return [processed[target-num[i]]+1,i+1]
        processed[num[i]]=i
        
A = [0,4,3,0]
target = 0
print two_sum(A,target)   