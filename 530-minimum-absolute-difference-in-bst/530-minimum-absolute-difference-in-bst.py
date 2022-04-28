# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    curr=pre=math.inf
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return
        
        self.getMinimumDifference(root.left)
        self.curr=min(self.curr,abs(root.val-self.pre))
        self.pre=root.val
        self.getMinimumDifference(root.right)
        
        return self.curr
        