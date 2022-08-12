# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.sol2(root,-math.inf,math.inf)
    
    def sol2(self,root,min_,max_):
        if root==None:
            return True
        if root.val>=max_ or root.val<=min_:
            return False
        
        return self.sol2(root.left,min_,root.val) and self.sol2(root.right,root.val,max_)
        

class Solution2:
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