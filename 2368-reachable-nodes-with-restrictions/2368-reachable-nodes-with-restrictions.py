class Solution:
    def __init__(self):
        self.__cnt=0
        
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph={i:[] for i in range(n)}
        
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        
        restrict=set()
        for i in restricted:
            restrict.add(i)
            
        self.dfs(0,graph,restrict,set())
        return self.__cnt
    
    def dfs(self,i,graph,restrict,vis):
        vis.add(i)
        self.__cnt+=1
            
        for node in graph[i]:
            if node not in vis and node not in restrict:
                self.dfs(node,graph,restrict,vis)