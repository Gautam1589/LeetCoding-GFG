# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
        
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root==None:
            return None
        
        temp=root.right
        root.right=root.left
        root.left=None
        
        t=root
        while t.right!=None:
            t=t.right
        t.right=temp
        
        self.flatten(root.right)
        self.flatten(root.left)
        
        
        
        

        
        