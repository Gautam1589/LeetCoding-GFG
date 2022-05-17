# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.__ans=0
        self.dfs1(original,cloned,target)
        return self.__ans
    
    def dfs1(self,original,cloned,target):
        if original==None or cloned==None:
            return 
        
        if original.val==target.val:
            self.__ans=cloned
        
        self.dfs1(original.left,cloned.left,target)
        self.dfs1(original.right,cloned.right,target)
    
        