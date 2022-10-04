from collections import defaultdict, deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr)==1:
            return 0
        
        graph = defaultdict(list)
        for i in range(len(arr)):
            graph[arr[i]].append(i)
            
        queue=deque()
        queue.append(0)
        steps=0
        
        while queue: 
            steps+=1
            size = len(queue)
            for i in range(size):
                j=queue.popleft()
                
                if j-1>=0 and arr[j-1] in graph:
                    queue.append(j-1)
                    
                if j+1<len(arr) and arr[j+1] in graph:
                    if j+1==len(arr)-1:
                        return steps
                    queue.append(j+1)
                    
                if arr[j] in graph:
                    for x in graph[arr[j]]:
                        if x!=j:
                            if x==len(arr)-1:
                                return steps
                            queue.append(x)
                    del graph[arr[j]]
            
        return steps
                
                        
            
            
            