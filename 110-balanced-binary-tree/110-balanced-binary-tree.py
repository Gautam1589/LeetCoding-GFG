# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        return self.check_height(root)!=-1
    
    def check_height(self,root):
        if root==None:
            return 0
        
        l=self.check_height(root.left)
        r=self.check_height(root.right)
        
        if abs(l-r)>1 or l==-1 or r==-1:
            return -1
        return 1+max(l,r)