# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        #reverse inorder (right-> root-> left)
        self.curr=0
        return self.dfs(root)
    
    def dfs(self,root):
        if root==None:
            return None
        
        self.dfs(root.right)
        
        self.curr+=root.val
        root.val=self.curr
        
        self.dfs(root.left)
        
        return root