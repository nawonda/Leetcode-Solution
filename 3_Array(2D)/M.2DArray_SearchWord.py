'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''

def exist(board, word):
        solution = False
        for i in range(0,len(board)):
            for j in range(0, len(board[0])):
                solution = solution or existRec(board, word, i, j, 0)
        return solution
        
def existRec(board, word, row, col, index):
    #base
    if row < 0 or row>=len(board) or col<0 or col>=len(board[0]) or  board[row][col]!=word[index]:
        return False
    
    #base
    if index==len(word)-1:
        return True
    
    #mark seen
    board[row][col] = "$"
    
    #search recursively
    solution = existRec(board, word, row-1, col, index+1) or existRec(board, word, row+1, col, index+1) or existRec(board, word, row, col-1, index+1) or existRec(board, word, row, col+1, index+1)
    
    #set it back
    board[row][col] = word[index]
    return solution