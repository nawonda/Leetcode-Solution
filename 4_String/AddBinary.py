'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''

def system_binary_sum(str1,str2):
    return bin(int(str1)+int(str2))


def addBinary(a, b):
        solution = []
        sum = 0
        for i in range(0,max(len(a),len(b))):
            if i < len(a) and a[len(a)-1-i]=='1':
                sum += 1
            if i < len(b) and b[len(b)-1-i]=='1':
                sum += 1
            solution.insert(0,str(sum%2))
            sum /= 2#for the next
        if sum >0:
            solution.insert(0,str(sum%2))
        return ''.join(solution)

    
str1 = '011'
str2 = '101'

#print system_binary_sum(str1,str2)
print addBinary(str1,str2)