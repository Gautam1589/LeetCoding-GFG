# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    global maxdia
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #O(N)-time
        self.maxdia=0
        self.dfs(root,0)
        return self.maxdia
        
        def maxdepth(root):
            if root==None:
                return 0
            left=maxdepth(root.left)
            right=maxdepth(root.right)
            return 1+max(left,right)
        
        if root==None:
            return -1
        left=diameterofBinaryTree(self,root.left)
        right=diameterofbinaryTree(root.right)
        res=max(left,right)
        
        hl=maxdepth(root.left)
        hr=maxdepth(root.right)
        return max(res,hl-hr)
    
    def dfs(self,root,curr_dia):
        if root==None:
            return 0
        
        left_h=self.dfs(root.left,curr_dia)
        right_h=self.dfs(root.right,curr_dia)
        
        curr_dia=left_h+right_h
        self.maxdia=max(self.maxdia,curr_dia)
        return max(left_h,right_h)+1
        
        
        
        
        
        
        
        