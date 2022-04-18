# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from heapq import *
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.max_heap=[]
        self.cnt=0
        self.dfs(root,k)
        return -self.max_heap[0]
        
    def dfs(self,root,k):
        if root==None:
            return None
        
        self.dfs(root.left,k)
        
        if self.cnt<k:
            heappush(self.max_heap,-root.val)
            self.cnt+=1
        else:
            if root.val<(-self.max_heap[0]):
                heappush(self.max_heap,-root.val)
        
        self.dfs(root.right,k)
        
            