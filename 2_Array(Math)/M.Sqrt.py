'''
Implement int sqrt(int x).

Compute and return the square root of x.
'''

def sqrt(x):
        if x < 0: 
            return -1
        begin = 0
        end = x
        while begin < end:
            midpoint = (begin+end+1)/2
            if midpoint* midpoint ==x:
                return midpoint
            if midpoint* midpoint < x:
                begin = midpoint
            else:
                end = midpoint - 1
        return begin