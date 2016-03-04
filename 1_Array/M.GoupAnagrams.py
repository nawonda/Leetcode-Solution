'''
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''

def anagrams(arr):
    n = len(arr)    
    hash = {}
       
    for i in range(n):    
        key = ''.join(sorted(arr[i]))
        
        if key not in hash: 
            hash[key] = [i]            
        else:
            hash[key].append(i)

    for k in hash:
        for j in hash[k]:
            print arr[j]
    
    
    
arr = ["cat", "dog", "tac", "god", "act"]
anagrams(arr)
