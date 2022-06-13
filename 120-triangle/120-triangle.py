class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.memoise(0,0,triangle,{})
    
    def memoise(self,i,j,triangle,dp):
        if i==len(triangle):
            dp[(i,j)]=0
            return 0
        
        if (i,j) in dp:
            return dp[(i,j)]
        
        dp[(i,j)]=min(triangle[i][j]+self.memoise(i+1,j,triangle,dp),triangle[i][j]+self.memoise(i+1,j+1,triangle,dp))
        return dp[(i,j)]