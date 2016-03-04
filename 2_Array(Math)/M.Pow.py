'''
We can do this problem in O(log n) by applying Xn=Xn/2⋅Xn/2 or if n is odd Xn=X(n−1)/2⋅X(n−1)/2⋅X. 
'''

def pow(x, n):
        if x==0 or x==1 or n==1:
            return x # We have the problem of 0^0 (that is not 
                     # well-defined), we choose to return 0
        if x == -1:
            if n%2 ==0:
                return 1
            else:
                return -1
        
        if n == 0:
            return 1
        
        if n < 0:
            return 1/pow(x,-n)
        
        val = pow(x,n//2)
        
        if n%2 ==0:
            return val*val
        
        return val*val*x

print  pow(-3,3)