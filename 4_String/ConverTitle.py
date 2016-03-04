'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
'''
import string

def convert(A):
    C = list(string.ascii_uppercase)

    temp = []
    while A > 0:
        temp.append(A%26)
        A = A//26
    result = ""
    
    i = len(temp)
    while i > 0:
        result = result + str(C[temp.pop()-1])
        i -= 1
    
    return result

print convert(28)