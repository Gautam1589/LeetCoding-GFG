import math
from heapq import *

class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        dist=[math.inf]*(V)
        vis=[False]*(V)
        
        minheap=[]
        dist[S]=0
        vis[S]=True
        heappush(minheap,(S,0))
        
        while minheap:
            currnode,currdist=heappop(minheap)
            for i in adj[currnode]:
                if vis[i[0]]==False and currdist+i[1]<dist[i[0]]:
                    dist[i[0]]=currdist+i[1]
                    vis[i[0]]==True
                    heappush(minheap,(i[0],dist[i[0]]))
        
        return dist
                    
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends