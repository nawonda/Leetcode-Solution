'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*n.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
Make sure the returned list of strings are sorted.
'''

class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, A):
        self.result = set()
        self.generateParenthesisHelper(A,["("])
        return sorted(self.result)
        
    def generateParenthesisHelper(self,n,parentheses):
        if len(parentheses) == n*2:
            self.result.add(''.join(parentheses))
            return
        
        if parentheses.count('(') < n:
            self.generateParenthesisHelper(n,parentheses + ["("])
            
        if parentheses.count(')') < parentheses.count('('):    
            self.generateParenthesisHelper(n,parentheses + [")"])