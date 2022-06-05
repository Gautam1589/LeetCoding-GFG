class Solution:
    #   global ans
    
    def totalNQueens(self, n: int) -> List[List[str]]:
        #self.ans=0
        return self.solve(0,set(),set(),set(),n)
        #return self.ans
    
    def solve(self,row,cols,diag,anti_diag,n):
        if row==n:
            return 1
        ans=0
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
        
                ans+=self.solve(row+1,cols,diag,anti_diag,n)
                
                cols.remove(curr_col)
                diag.remove(curr_diag)
                anti_diag.remove(curr_anti_diag)
        return ans