'''
Given A, how many structurally unique BST’s (binary search trees) that store values 1...A?

Example :

Given A = 3, there are a total of 5 unique BST’s.


   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

hint:

0  |   1  |    1     2  |  1     2     3   |   1     2     3    4
1      1      1*1 + 1*1   1*2 + 1*1 + 2*1     1*5   1*2   2*1  5*1
1      1         2               5                  14

'''
  def numTrees(A):
        result = {0:1,1:1}
        if A == 0 or A == 1:
            return result[A]
                     
        for i in range(2,A+1):
            result[i] = 0
            for k in range(1,i+1):
                result[i] += result[k - 1] * result[i - k]
                
        return result[A]

    
    
        
