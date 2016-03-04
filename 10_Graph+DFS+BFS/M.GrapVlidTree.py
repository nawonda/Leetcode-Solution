'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

For example:

Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.
'''
#DFS
def check_valid(n,edges):
    
    adj_lsit = {}
    
    for edge in edges:
        if adj_lsit[edge[0]]:
            adj_lsit[edge[0]].append(edge[1])
        else:
            adj_lsit[edge[0]] = [edge[1]]
            
        if adj_lsit[edge[1]]:
            adj_lsit[edge[1]].append(edge[0])
        else:
            adj_lsit[edge[1]] = [edge[0]]            
    
    visited = [0]*n
    
    if not check_helper(n,edges,0,-1,visited,adj_list):
        return False
    
    if min(visited) == 0:
        return False
    
    return True
    
    
def check_helper(n,edges,rootId,parentId,visited,adj_list):    
    if visited[rootId]:
        return False
    
    visited[rootId] = 1
    
    neighbors = adj_list[rootId]
    
    for neighbor in neighbors:
        if neighbor != rootId and not check_helper(n,edges,neighbor,rootId,visited,adj_list):
            return False
        
    return True
        
        
'''
----------------------------
'''        
#Quick-Union
class Solution(object):  
    def validTree(self, n, edges):  
        root = [i for i in range(n)]  
        for i in edges:  
            root1 = self.find(root, i[0])  
            root2 = self.find(root, i[1])  
            if root1 == root2:  
                return False  
            else:  
                root[root1] = root2  
        return len(edges) == n - 1  
          
    def find(self, root, e):  
        if root[e] == e:  
            return e  
        else:  
            return self.find(root, root[e])  
        
        
        
        
        