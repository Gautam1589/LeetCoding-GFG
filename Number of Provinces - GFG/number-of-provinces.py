#User function Template for python3

class Solution:
    def numProvinces(self, adj, V):
        # code here 
        vis=set()
        cnt=0
        for v in range(V):
            if v not in vis:
                self.dfs(adj,v,vis)
                cnt+=1
        return cnt
    
    def dfs(self,adj,v,vis):
        vis.add(v)
        
        for j in range(len(adj[0])):
            if adj[v][j]==1 and j not in vis:
                self.dfs(adj,j,vis)
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends