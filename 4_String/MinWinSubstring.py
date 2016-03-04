'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
'''

def min_win(S,T):
    #len(T)
    #loop S, first find add right to contain all then throw from the left
    dic = {t:0 for t in T}; start = 0; end = len(T)-1; ans = []
    for i in range(len(S)):
        end = i
        if S[i] in dic:
            dic[S[i]] += 1
        if min(dic.itervalues()) > 0:            
            start,dic = optimize(dic,S,start,i)
            ans.append([start,end])
                        
    return ans        


def optimize(dic,S,start,i):
    for j in range(start,i):
        if S[j] not in dic:
            start = j+1
        else:
            dic[S[j]] -= 1
            if min(dic.itervalues()) <= 0:                
                dic[S[j]] += 1
                break
            else:
                start = j+1                
    return start,dic            
        

S = "ADOBECODEBANC"
T = "ABC"


print min_win(S,T)


