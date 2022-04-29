# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    global range_sum
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.range_sum=0
        self.find_node(root,low,high)
        return self.range_sum
        
        
    def find_node(self,root,p,q):
        if root==None:
            return 
        
        if root.val in range(p,q+1):
            self.range_sum+=root.val
        
        self.find_node(root.left,p,q)
        self.find_node(root.right,p,q)
        
#         if root.val>p and root.val>q:
#             self.find_node(root.left,p,q)
        
#         if root.val<p and root.val<q:
#             self.find_node(root.right,p,q)
        
#         if root.val>=p and root.val<=q:
#             self.find_node(root.left,p,q)
#             self.find_node(root.right,p,q)
      