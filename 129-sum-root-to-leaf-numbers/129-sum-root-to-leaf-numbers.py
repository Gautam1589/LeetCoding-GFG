# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    global res
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res=0
        self.dfs(root,'')
        return self.res
    
    def dfs(self,root,temp):
        if root.left==None and root.right==None:
            temp+=str(root.val)
            self.res+=int(temp)
            return
        
        temp+=str(root.val)
        if root.left:
            self.dfs(root.left,temp)
        if root.right:
            self.dfs(root.right,temp)