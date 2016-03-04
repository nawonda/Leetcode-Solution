'''
Given a string, write a function that uses recursion to output a list of all the possible permutations of that string.
For example, given s='abc' the function should return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
Note: If a character is repeated, treat each occurence as distinct, for example an input of 'xxx' would return a list with 6 "versions" of 'xxx'
'''

result = []

def permute(A,pre):
    #base
    if len(A) <= 0:
        result.append(pre)
        return 
    
    #permute    
    for i in range(len(A)):        
        permute(A[0:i]+A[i+1:],pre + A[i])

        
A = 'abcd'        
permute(A,"")
print result