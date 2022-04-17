# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root==None:
            return None
        
        if key>root.val:
            root.right=self.deleteNode(root.right,key)
        elif key<root.val:
            root.left=self.deleteNode(root.left,key)
        else:
            if root.left and root.right:
                left_max=self.find_max(root.left)
                root.val=left_max
                root.left=self.deleteNode(root.left,left_max)
                return root
            elif root.left:
                return root.left
            elif root.right:
                return root.right
            else:
                return None
        
        return root
    
    def find_max(self,root):
        if root.right:
            return self.find_max(root.right)
        else:
            return root.val