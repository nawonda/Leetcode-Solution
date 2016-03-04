'''
Find the longest increasing subsequence of a given sequence / array.

In other words, find a subsequence of array in which the subsequence’s elements are in strictly increasing order, and in which the subsequence is as long as possible. 
This subsequence is not necessarily contiguous, or unique.
In this case, we only care about the length of the longest increasing subsequence.

Example :

Input : [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
Output : 6
The sequence : [0, 2, 6, 9, 13, 15] or [0, 4, 6, 9, 11, 15] or [0, 4, 6, 9, 13, 15]
'''

#Hint use a hash to keep count of number of elements less then ith 

'''
{0: 1}
{0: 1, 8: 2}
{0: 1, 8: 2, 4: 2}
{0: 1, 8: 2, 4: 2, 12: 3}
{0: 1, 8: 2, 2: 2, 4: 2, 12: 3}
{0: 1, 2: 2, 4: 2, 8: 2, 10: 3, 12: 3}
{0: 1, 2: 2, 4: 2, 6: 3, 8: 2, 10: 3, 12: 3}
{0: 1, 2: 2, 4: 2, 6: 3, 8: 2, 10: 3, 12: 3, 14: 4}
{0: 1, 1: 2, 2: 2, 4: 2, 6: 3, 8: 2, 10: 3, 12: 3, 14: 4}
{0: 1, 1: 2, 2: 2, 4: 2, 6: 3, 8: 2, 9: 4, 10: 3, 12: 3, 14: 4}
{0: 1, 1: 2, 2: 2, 4: 2, 5: 3, 6: 3, 8: 2, 9: 4, 10: 3, 12: 3, 14: 4}
{0: 1, 1: 2, 2: 2, 4: 2, 5: 3, 6: 3, 8: 2, 9: 4, 10: 3, 12: 3, 13: 5, 14: 4}
{0: 1, 1: 2, 2: 2, 3: 3, 4: 2, 5: 3, 6: 3, 8: 2, 9: 4, 10: 3, 12: 3, 13: 5, 14: 4}
{0: 1, 1: 2, 2: 2, 3: 3, 4: 2, 5: 3, 6: 3, 8: 2, 9: 4, 10: 3, 11: 5, 12: 3, 13: 5, 14: 4}
{0: 1, 1: 2, 2: 2, 3: 3, 4: 2, 5: 3, 6: 3, 7: 4, 8: 2, 9: 4, 10: 3, 11: 5, 12: 3, 13: 5, 14: 4}
{0: 1, 1: 2, 2: 2, 3: 3, 4: 2, 5: 3, 6: 3, 7: 4, 8: 2, 9: 4, 10: 3, 11: 5, 12: 3, 13: 5, 14: 4, 15: 6}
'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        hash_map = {}
        
        for i in A:
            count = 1
            temp = []
            for k in hash_map:
                if k < i:
                    temp.append(hash_map[k])
            count += max(temp) if temp else 0
            
            hash_map[i] = count
            
        return max(hash_map.values())    
    
A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]    
print Solution().lis(A)    
    
    