# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.res=[]
        self.dfs(root)
        
        s=set(self.res)
        n=len(s)
        
        if n==1:
            return -1
        
        s=list(s)
        s.sort()
        for i in range(1,n):
            if s[i]!=s[i-1]:
                return s[i]
        return -1
            
    
    def dfs(self,root):
        if root==None:
            return
        
        self.dfs(root.left)
        
        self.res.append(root.val)
        
        self.dfs(root.right)
 