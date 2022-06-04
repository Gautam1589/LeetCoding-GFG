class Solution:
    global ans
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.ans=[]
        initial=[['.']*n for i in range(n)]
        # wrong new=[['.']*n]*n one list created n times with same address
        self.solve(0,set(),set(),set(),initial,n)
        return self.ans
    
    def solve(self,row,cols,diag,anti_diag,board,n):
        if row==n:
            self.ans.append(self.arrange(board))
            return
        
        for j in range(n):
            curr_col=j
            curr_diag=row-j
            curr_anti_diag=row+j
            if curr_col in cols or curr_diag in diag or curr_anti_diag in anti_diag:
                continue
            else:
                #place queen
                cols.add(curr_col)
                diag.add(curr_diag)
                anti_diag.add(curr_anti_diag)
                board[row][curr_col]='Q'
                self.solve(row+1,cols,diag,anti_diag,board,n)
                
                board[row][curr_col]='.'
                cols.remove(curr_col)
                diag.remove(curr_diag)
                anti_diag.remove(curr_anti_diag)
            
    def arrange(self,board):
        new_board=[]
        for i in board:
            new_board.append(''.join(i))
        return new_board
        
            
            
        
        