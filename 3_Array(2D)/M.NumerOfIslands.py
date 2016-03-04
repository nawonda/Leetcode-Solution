'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''

def number_islands(A):
    
    #for for, skip "$" and "0", only conside "1"
    #mark $
    
    count = 0
    for i in range(len(A)):        
        for j in range(len(A[0])):            
            if A[i][j] == 1:
                count += 1
                check_water(A,i,j)
    return count
                
                
def check_water(A,i,j):    
    for k in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
        x,y = k        
        if len(A) > x >= 0 and len(A[0]) > y >= 0:
            if A[x][y] == 1:
                A[x][y] = "$"
                check_water(A,x,y)
            

#A = [
#[1,1,1,1,0],
#[1,1,0,1,0],
#[1,1,0,0,0],
#[0,0,0,0,0]
#]            
    
A = [
[1,1,0,0,0],
[1,1,0,0,0],
[0,0,1,0,0],
[0,0,0,1,1]
]       
print number_islands(A)                
                
    