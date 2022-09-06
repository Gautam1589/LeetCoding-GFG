# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if self.solve(root)==False:
            return None
        return root
    
    def solve(self,root):
        if root==None:
            return False
        
        if root.left==None and root.right==None:
            if root.val==0:
                return False
            return True
        
        left=self.solve(root.left)
        if left==False:
            root.left=None
        right=self.solve(root.right)
        if right==False:
            root.right=None
        if root.val==1:
            return True
        else:
            if left or right:
                return True
            return False
            
        
       
        
        
        