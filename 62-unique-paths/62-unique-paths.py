class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.memoise(0,0,m,n,{})
    
    def memoise(self,i,j,m,n,dp):
        if i==m-1 and j==n-1:
            dp[(i,j)]=1
            return 1
        
        if (i,j) in dp:
            return dp[(i,j)]
        
        if i>=m or j>=n:
            dp[(i,j)]=0
            return 0
        
        dp[(i,j)]=self.memoise(i+1,j,m,n,dp)+self.memoise(i,j+1,m,n,dp)
        return dp[(i,j)]
        