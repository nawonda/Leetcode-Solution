'''
Given a collection of unique numbers, return all possible permutations.
'''

class Solution:
    def permute(self,A):        
        return self.permutation_helper(A,[],[])
    
    def permute_helper(self,A,pre,result):
        if len(A) == 0:
            result.append(pre)
            return 
    
        for i in range(len(A)):
            self.permute_helper(A[0:i]+A[i+1:],pre+A[i],result)
        
        #if there is no unique condition                
#        unique_set = set()
#        for i,c in enumerate(result):
#            if tuple(c) not in unique_set:
#                unique_set.add(tuple(c))        
#        
#        return list(unique_set)
        
        
        
        return result