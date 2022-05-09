class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        visited={}
        discovered_time=[0]*n
        lowest_time=[0]*n
        
        timer=0
        graph={i:[] for i in range(n)}
        
        for edge in connections:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        critical_connections=[]
        for node in range(n):
            if node not in visited:
                self.dfs(node,-1,graph,visited,lowest_time,discovered_time,critical_connections,timer)
                
        return critical_connections
    
    def dfs(self,node,parent,graph,vis,low,dis,cc,timer):
        vis[node]=True
        low[node]=timer
        dis[node]=timer
        timer+=1
        
        for nbr in graph[node]:
            if nbr==parent:
                continue
            elif nbr not in vis:
                self.dfs(nbr,node,graph,vis,low,dis,cc,timer)
                low[node]=min(low[node],low[nbr])
                
                if low[nbr]>dis[node]:
                    cc.append([node,nbr])
            else:
                #backedge
                low[node]=min(low[node],dis[nbr])