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
        
#1 2 3 4 5 6          
def preorder(root):
    if root:        
        print root.key,
        preorder(root.left)
        preorder(root.right)

#3 2 4 1 5 6   
def inorder(root):
    if root:
        inorder(root.left)
        print root.key,
        inorder(root.right)
        
#3 4 2 6 5 1        
def postorder(root):
    if root:
        postorder(root.left)        
        postorder(root.right)  
        print root.key,
                
'''
iteration
'''

def preorder_2(root):    
    stack = []
    result = []
    while root or len(stack) > 0:
        if root:
            result.append(root.key)
            stack.append(root)
            root = root.left
        else:
            root = stack.pop().right
    
    return result
    
def inorder_2(root):
    
    result = []
    stack = []
    while root or len(stack) > 0:
        if root:
            stack.append(root)
            root = root.left        
        else:
            root = stack.pop()
            result.append(root.key)
            root = root.right
    
    return result
    

def postorder_2(root):
        solution = []
        used = set()
        stack = []
        if root != None:
            stack.append(root)
        while len(stack)>0:
            node = stack.pop()
            if node in used:
                solution.append(node.val)
            else:
                used.add(node)
                stack.append(node)
                if node.right != None:
                    stack.append(node.right)
                if node.left != None:
                    stack.append(node.left)
        return solution    

root = Node(1)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.right = Node(6)

print inorder_2(root)
