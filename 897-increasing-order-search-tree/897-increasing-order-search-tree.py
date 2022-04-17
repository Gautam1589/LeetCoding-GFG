# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.dummy_node=TreeNode(0)
        self.head=self.dummy_node
        
        self.inorder(root)
        
        return self.head.right
    
    def inorder(self,root):
        if root==None:
            return None
        
        self.inorder(root.left)
        
        self.dummy_node.right=TreeNode(root.val)
        self.dummy_node=self.dummy_node.right
        
        self.inorder(root.right)
        
        