'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
'''

class Node:
    def __init__(self, key):
        self.key =  key
        self.left = None
        self.right = None
 
def findPath( root, path, k):
 
    if root is None:
        return False
 
    path.append(root.key)

    if root.key == k :
        return True

    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right!= None and findPath(root.right, path, k))):
        return True
      
    path.pop()
    return False
 
def findLCA(root, n1, n2):

    path1 = []
    path2 = []
    
    if (not findPath(root, path1, n1) or not findPath(root, path2, n2)):
        return -1

    i = 0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
 
print "LCA(4, 5) = %d" %(findLCA(root, 4, 5,))
print "LCA(4, 6) = %d" %(findLCA(root, 4, 6))
print "LCA(3, 4) = %d" %(findLCA(root,3,4))
print "LCA(2, 4) = %d" %(findLCA(root,2, 4))