'''
Given a set of distinct integers, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    
    def subsets(self, S):
        def dfs(depth, start, valuelist):
            res.append(valuelist)
            if depth == len(S): return
            print start
            for i in range(start, len(S)):            
                dfs(depth+1, i+1, valuelist+[S[i]])#once add something to it, it became a new object
        
        res = []
        dfs(0, 0, [])
        return res
        
        
S = [1,2,3]        

print Solution().subsets(S)