class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m=len(heights)
        n=len(heights[0])
        
        pacific=[[0]*n for i in range(m)]
        atlantic=[[0]*n for i in range(m)]
        ans=[]
        
        for j in range(n):
            self.dfs(0,j,pacific,heights,-1)
            self.dfs(m-1,j,atlantic,heights,-1)
            
        for i in range(m):
            self.dfs(i,0,pacific,heights,-1)
            self.dfs(i,n-1,atlantic,heights,-1)
        
        for i in range(m):
            for j in range(n):
                if pacific[i][j] & atlantic[i][j]:
                    ans.append([i,j])
        return ans
    
    def dfs(self,r,c,arr,h,prev):
        if r<0 or c<0 or r>=len(h) or c>=len(h[0]):
            return
        
        if h[r][c]<prev:
            return 
        
        if arr[r][c]==1:
            return
        
        arr[r][c]=1
        self.dfs(r+1,c,arr,h,h[r][c])
        self.dfs(r,c+1,arr,h,h[r][c])
        self.dfs(r,c-1,arr,h,h[r][c])
        self.dfs(r-1,c,arr,h,h[r][c])
        
        