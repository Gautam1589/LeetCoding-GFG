# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #O(n)
        return self.solve(root,-math.inf,math.inf)
    
        #O(n)+O(n)
        res=[]
        self.inorder(root,res)
        for i in range(len(res)-1):
            if res[i]>=res[i+1]:
                return False
        return True
        
    def solve(self,root,ll,ul):
        if root==None:
            return True
        
        if root.val>ll and root.val<ul:
            return self.solve(root.left,ll,root.val) and self.solve(root.right,root.val,ul)
        
        return False
        
    def inorder(self,root,res):
        if root==None:
            return 
    
        self.inorder(root.left,res)
        res.append(root.val)
        self.inorder(root.right,res)
        
        return res
        