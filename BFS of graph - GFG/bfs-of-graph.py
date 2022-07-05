#User function Template for python3
from collections import deque
class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        ans=[]
        queue=deque()
        queue.append(0)
        vis=set()
        vis.add(0)
        
        while queue:
            node=queue.popleft()
            ans.append(node)
            
            for i in adj[node]:
                if i not in vis:
                    queue.append(i)
                    vis.add(i)
                
        return ans

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends