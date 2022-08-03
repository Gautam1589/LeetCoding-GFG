class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        return self.memoise(0,0,obstacleGrid,m,n,{})
    
    def memoise(self,i,j,matrix,m,n,dp):
        if i>=m or j>=n:
            dp[(i,j)]=0
            return 0
        
        if matrix[i][j]==1:
            dp[(i,j)]=0
            return 0
        
        if i==m-1 and j==n-1:
            dp[(i,j)]=1
            return 1
        
        if (i,j) in dp:
            return dp[(i,j)]
        
        dp[(i,j)]=self.memoise(i+1,j,matrix,m,n,dp)+self.memoise(i,j+1,matrix,m,n,dp)
        return dp[(i,j)]
        