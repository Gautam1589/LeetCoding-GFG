class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        d={}
        
        graph={i:[] for i in range(n)}
        
        for i in roads:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
            
        arr=[]
        for i in range(n):
            arr.append(i)
            
        max_rank=0
        for i in range(n):
            for j in range(n):
                curr=len(graph[arr[i]])
                if i!=j:
                    curr+=len(graph[arr[j]])
                    if arr[i] in graph[arr[j]]:
                        curr-=1
                max_rank=max(max_rank,curr)
        
        return max_rank
            
            