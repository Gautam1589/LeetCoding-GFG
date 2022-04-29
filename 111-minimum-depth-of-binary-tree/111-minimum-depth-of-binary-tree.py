# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        #return self.recursion(root)
        return self.bfs(root)
    
    def bfs(self,root):
        if root==None:
            return 0
        
        path=1
        queue=deque()
        queue.append(root)
        while queue:
            level_size=len(queue)
            for i in range(level_size):
                node=queue.popleft()
                if node.left==None and node.right==None:
                    return path
                
                if node.left!=None:
                    queue.append(node.left)
                if node.right!=None:
                    queue.append(node.right)
            path+=1        
                    
        
    def recursion(self,root):
        if root==None:
            return 0
        
        l=self.recursion(root.left)
        r=self.recursion(root.right)
        
        if l==0 or r==0:
            return 1+max(l,r)
        
        return 1+min(l,r)
        
        