# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    global allsol
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.allsol=[]
        self.dfs(root,'')
        return self.allsol
    
    def dfs(self,root,currsol):
        if root.left==None and root.right==None:
            currsol+=str(root.val)
            self.allsol.append(currsol[:])
            return 
        
        currsol+=str(root.val)+'->'
        if root.left!=None:
            self.dfs(root.left,currsol)
        if root.right!=None:
            self.dfs(root.right,currsol)
        