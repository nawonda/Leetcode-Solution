def factorial1(n):
    if n == 0:
        return 1
    
    # Recursion!
    else:
        return n * factorial1(n-1)


factorial_memo = {}

def factorial2(k):
    
    if k < 2: 
        return 1
    
    if not k in factorial_memo:
        factorial_memo[k] = k * factorial2(k-1)
        
    return factorial_memo[k]


from timeit import Timer

t1 = Timer(lambda: factorial1(100))
print t1.timeit(number=10000)
t2 = Timer(lambda: factorial2(100))
print t2.timeit(number=10000)