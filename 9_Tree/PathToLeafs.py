'''
         1
        / \
       2   5
      / \   \
     3   4   6
'''
class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        
        
def pathToLeafs(root,pre):
    
    if root.left == None and root.right == None:
        result.append(pre+[root.key])
    
    if root.left:
        pathToLeafs(root.left,pre+[root.key])    
    if root.right:
        pathToLeafs(root.right,pre+[root.key])    
    
    
root = Node(1)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(3)
root.left.right = Node(4)
root.left.right.left = Node(7)
root.right.right = Node(6)    
    
result = []    
pathToLeafs(root,[])    
print result