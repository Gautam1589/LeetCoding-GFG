# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        arr1=self.inorder(root1,[])
        arr2=self.inorder(root2,[])
        if arr1==arr2:
            return True
        return False
    
    def inorder(self,root,arr):
        if root==None:
            return
        
        self.inorder(root.left,arr)
        
        if root.left==None and root.right==None:
            arr.append(root.val)
        
        self.inorder(root.right,arr)
        
        return arr