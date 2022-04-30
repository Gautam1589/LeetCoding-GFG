class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph=collections.defaultdict(dict)
        
        for i in range(len(values)):
            graph[equations[i][0]][equations[i][1]]=values[i]
            graph[equations[i][1]][equations[i][0]]=1/values[i]
        
        res=[]
        for i in queries:
            res.append(self.dfs(graph,i[0],i[1],set()))
        
        return res
    
    def dfs(self,graph,src,target,vis):
        if src not in graph or target not in graph:
            return -1.0
        
        if target in graph[src]:
            return graph[src][target]
        
        for i in graph[src]:
            if i not in vis:
                vis.add(i)
                temp=self.dfs(graph,i,target,vis)
                if temp==-1:
                    continue
                else:
                    return temp*graph[src][i]
        
        return -1
                
                