class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        
        cnt=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    cnt+=self.bfs(grid,i,j,m,n)
                
    
        return cnt
    
    def bfs(self,grid,i,j,m,n):
        queue=deque()
        queue.append((i,j))
        grid[i][j]=0
        
        cnt=0
        while queue:
            r,c=queue.popleft()
            cnt+=1
            for i in range(m):
                if grid[i][c]==1:
                    queue.append((i,c))
                    grid[i][c]=0
                
            
            for j in range(n):
                if grid[r][j]==1:
                    queue.append((r,j))
                    grid[r][j]=0
        
                  
        return 0 if cnt ==1 else cnt