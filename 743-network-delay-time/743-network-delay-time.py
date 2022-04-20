from heapq import *
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #Dijkstra
        weight_matrix=[[-1]*(n+1) for i in range(n+1)]
        for edge in times:
            u,v,w=edge[0],edge[1],edge[2]
            weight_matrix[u][v]=w
            
        return self.dijkstra(weight_matrix,n,k)
    
    def dijkstra(self,matrix,n,src):
        dist=[math.inf]*(n+1)
        vis=[False]*(n+1)
        
        min_heap=[]
        heappush(min_heap,(0,src))
        dist[src]=0
        
        while min_heap:
            curr_dist,curr_node=heappop(min_heap)
            if vis[curr_node]==False:
                vis[curr_node]=True
                
                for j in range(n+1):
                    if matrix[curr_node][j]!=-1 and curr_dist+matrix[curr_node][j]<dist[j]:
                        dist[j]=curr_dist+matrix[curr_node][j]
                        heappush(min_heap,(dist[j],j))
        
        max_=max(dist[1:])
        if max_==math.inf:
            return -1
        return max_