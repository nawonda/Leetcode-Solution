'''
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

def strStr(A,B):
    n = len(B)
    for i in range(len(A)):
        if A[i:i+n] == B:
            return i
    return -1

A = "Samantha"
B = "mans"

print strStr(A,B)