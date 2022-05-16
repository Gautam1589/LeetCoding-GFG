from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        return self.bfs(grid)
    
    def bfs(Self,grid):
        n=len(grid)
        if grid[0][0]==1 or grid[n-1][n-1]==1:
            return -1
        
        direction=[[0,1],[0,-1],[1,0],[-1,0],[-1,-1],[1,1],[1,-1],[-1,1]]
        queue=deque()
        queue.append((0,0,1))
        
        while queue:
            i,j,dist=queue.popleft()
            if i==n-1 and j==n-1:
                return dist
            
            for k in direction:
                I=i+k[0]
                J=j+k[1]
                if I<0 or I>=n or J<0 or J>=n:
                    continue
                
                if grid[I][J]==0:
                    queue.append((I,J,dist+1))
                    grid[I][J]=2
                
        return -1
        