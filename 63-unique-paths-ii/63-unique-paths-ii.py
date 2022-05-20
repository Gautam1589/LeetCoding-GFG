class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.dp={}
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        #memoisation
        return self.solve(0,0,m,n,obstacleGrid) #O(mn) time
        #top-to-down
        return self.table(m,n) #O(mn) time 
        
    def solve(self,i,j,m,n,grid):
        if i>=m or j>=n:
            self.dp[(i,j)]=0
            return 0
        
        if grid[i][j]==1:
            self.dp[(i,j)]=0
            return 0
        
        if i==m-1 and j==n-1:
            self.dp[(i,j)]=1
            return 1
        
        if (i,j) in self.dp:
            return self.dp[(i,j)]
        
        if i>=m or j>=n:
            self.dp[(i,j)]=0
            return 0
        
        #if i+1<m and grid[i+1][j]==0:
        ans=self.solve(i+1,j,m,n,grid)
        #if j+1<n and grid[i][j+1]==0:
        ans+=self.solve(i,j+1,m,n,grid)
        self.dp[(i,j)]=ans
        return self.dp[(i,j)]
    
    def table(self,m,n):
        dp=[[1]*n for j in range(m)]
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
                
        return dp[m-1][n-1]