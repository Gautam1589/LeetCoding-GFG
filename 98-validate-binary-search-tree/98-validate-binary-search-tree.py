# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans=[]
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.sol1(root)
        for i in range(1,len(self.ans)):
            if self.ans[i]<=self.ans[i-1]:
                return False
        return True
        
    def sol1(self,root):
        if root==None:
            return None
        
        self.sol1(root.left)
        self.ans.append(root.val)
        self.sol1(root.right)