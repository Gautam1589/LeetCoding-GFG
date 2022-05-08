# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #return self.maxdepth(root)
        return self.bfs(root)
    
    def bfs(self,root):
        if root==None:
            return 0
        
        path=0
        queue=deque()
        queue.append(root)
        while queue:
            level_size=len(queue)
            for i in range(level_size):
                node=queue.popleft()
                
                if node.left!=None:
                    queue.append(node.left)
                if node.right!=None:
                    queue.append(node.right)
            path+=1 
        return path
    
    
    def maxdepth(self,root):
        if root==None:
            return 0
        l=self.maxdepth(root.left)
        r=self.maxdepth(root.right)
            
        return 1+max(l,r)
        