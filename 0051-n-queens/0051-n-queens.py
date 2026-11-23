class Solution(object):
    def isSafe(self, board, row, col):
        n=len(board)
        for j in range(col):
            if board[row][j]=='Q':
                return False
        for i in range(1,min(row,col)+1):
            if board[row-i][col-i]=='Q':
                return False
        for i in range(1,min(n-1-row,col)+1):
            if board[row+i][col-i]=='Q':
                return False
        return True
    
    def backtrack(self, board, col, ans):
        if col==len(board):
            ans.append(["".join(row) for row in board])
            return
        for row in range(len(board)):
            if self.isSafe(board,row,col):
                board[row][col]='Q'
                self.backtrack(board,col+1,ans)
                board[row][col]='.'

    def solveNQueens(self, n):
        ans=[]
        board=[['.']*n for _ in range(n)]
        self.backtrack(board,0,ans)
        return ans