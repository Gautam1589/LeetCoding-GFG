class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue=deque()
        queue.append((entrance[0],entrance[1],0))
        # maze[entrance[0]][entrance[1]]='+'
        dirn=[(-1,0),(0,-1),(1,0),(0,1)]
        
        while queue:
            i,j,d=queue.popleft()
            # print(i,j)
            if (i==0 or j==0 or i==len(maze)-1 or j==len(maze[0])-1) and (i!=entrance[0] or j!= entrance[1]):
                return d
            
            for x in dirn:
                I=i+x[0]
                J=j+x[1]
                
                if I<0 or J<0 or I>=len(maze) or J>=len(maze[0]) or maze[I][J]=='+':
                    continue
                queue.append((I,J,d+1))
                maze[I][J]='+'
        
        return -1