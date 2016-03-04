import math

def level_order(tree_list):
    
    n = int(math.log(((len(tree_list)-1)/2)+1,2))+1
    
    result = []
    end = 0
    
    for i in range(n):
        start = end
        end = 2*((2**i)-1)+1
        result.append(tree_list[start:end])
            
    return result

tree_list = [3,9,20,'#','#',15,7,'#','#',15,7,'#','#',15,7]    
#print level_order(tree_list) 

'''
Given a binary tree of integers, print it in level order. The output will contain space between the numbers in the same level, and new line between different levels. For example, if the tree is:

         1
        / \
       2   3
      / \   \
     4   5   6

The output should be:
1 
2 3 
4 5 6
'''


# Definition for a  binary tree node
class Node:
    def __init__(self, key):
        self.val =  key
        self.left = None
        self.right = None

def levelOrder(root):
    solution=[]
    if root == None:
        return solution
    levelToProcess =[root]
#    print levelToProcess
#    print len(levelToProcess)
    
    while len(levelToProcess)>0:
        numbersLevel =[]
        nextLevel = []
        for temp in levelToProcess:
            numbersLevel.append(temp.val)
            if temp.left != None:
                nextLevel.append(temp.left)
            if temp.right != None:
                nextLevel.append(temp.right)
        solution.append(numbersLevel)
        levelToProcess = nextLevel
    return solution    
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.right = Node(8) 

print levelOrder(root)
   
