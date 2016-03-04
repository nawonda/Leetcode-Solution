'''
In this interview excercise we will begin to get a feel of having to solve a single problem multiple ways!
Problem Statement
Implement a Fibonnaci Sequence in three different ways:

1. Recursively
2. Dynamically (Using Memoization to store results)
3. Iteratively

Function Output
Your function will accept a number n and return the nth number of the fibonacci sequence
Remember that a fibonacci sequence: 0,1,1,2,3,5,8,13,21,... starts off with a base case checking to see if n = 0 or 1, then it returns 1.
Else it returns fib(n-1)+fib(n+2).

'''
from timeit import Timer

def fib_rec(n):
    
    # Base Case
    if n == 0 or n == 1:
        return n
    
    # Recursion
    else:
        return fib_rec(n-1) + fib_rec(n-2)

def fib_iter(n):
    
    # Set starting point
    a = 0
    b = 1
    
    # Follow algorithm
    for i in range(n):
        
        a, b = b, a + b
        
    return a
    
    
# Instantiate Cache information
n = 10
cache = [None] * (n + 1)


def fib_dyn(n):
    
    # Base Case
    if n == 0 or n == 1:
        return n
    
    # Check cache
    if cache[n] != None:
        return cache[n]
    
    # Keep setting cache
    cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
    
    return cache[n]


def fibonacci(n, fib = [0, 1]):
    if n >= len(fib):
        for i in range(len(fib), n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]


t1 = Timer(lambda: fib_rec(10))
print t1.timeit(number=10000)
t2 = Timer(lambda: fib_iter(10))
print t2.timeit(number=10000)
t3 = Timer(lambda: fib_dyn(10))
print t3.timeit(number=10000)
t4 = Timer(lambda: fibonacci(10))
print t4.timeit(number=10000)

#0.42070889473
#0.0215950012207
#0.00859498977661
#0.00600504875183

