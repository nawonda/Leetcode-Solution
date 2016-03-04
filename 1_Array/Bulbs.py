'''
N light bulbs are connected by a wire. Each bulb has a switch associated with it, however due to faulty wiring, a switch also changes the state of all the bulbs to the right of current bulb. Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs. You can press the same switch multiple times.

Note : 0 represents the bulb is off and 1 represents the bulb is on.
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        count = 0
        state = 0 #state needed to be chekced
        for i in range(len(A)):            
            if A[i] == state:
                state = 1 - state 
                count += 1
        return count     