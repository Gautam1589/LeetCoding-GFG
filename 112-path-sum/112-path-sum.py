# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root==None:
            return False
        
        return self.dfs(root,targetSum)
    
    def dfs(self,root,target):
        if root==None:
            return False
        
        if target==root.val and root.left==None and root.right==None:
            return True
        
        if root.left==None and root.right==None:
            return False

        
        return self.dfs(root.left,target-root.val) or self.dfs(root.right,target-root.val)