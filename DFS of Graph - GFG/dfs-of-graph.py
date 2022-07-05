#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code  
        return self.dfs(adj,0,set(),[])
    
    def dfs(self,adj,node,vis,ans):
        vis.add(node)
        ans.append(node)
        
        for i in adj[node]:
            if i not in vis:
                vis.add(i)
                self.dfs(adj,i,vis,ans)
            
        return ans
                

#{ 
#  Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends