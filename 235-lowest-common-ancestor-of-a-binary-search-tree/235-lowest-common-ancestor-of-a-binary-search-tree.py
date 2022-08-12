# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val<=q.val:
            return self.sol1(root,p,q)
        else:
            return self.sol1(root,q,p)
        
    def sol1(self,root,p,q):
        if root.val>=p.val and root.val<=q.val:
            return root
        
        if root.val<p.val:
            return self.sol1(root.right,p,q)
        if root.val>q.val:
            return self.sol1(root.left,p,q)