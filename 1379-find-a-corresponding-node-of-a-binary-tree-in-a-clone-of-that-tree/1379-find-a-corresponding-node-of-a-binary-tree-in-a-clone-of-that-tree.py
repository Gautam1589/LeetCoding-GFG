# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        #self.__ans=0
        #self.dfs1(original,cloned,target)
        #return self.__ans
        return self.dfs2(original,cloned,target)
    
    def dfs1(self,original,cloned,target):
        if original==None or cloned==None:
            return 
        
        if original.val==target.val:
            self.__ans=cloned
            return
        
        self.dfs1(original.left,cloned.left,target)
        self.dfs1(original.right,cloned.right,target)
    
    def dfs2(self,original,cloned,target):
        if original==None or cloned==None:
            return None
        
        if original.val==target.val:
            return cloned
        
        left=self.dfs2(original.left,cloned.left,target)
        if left!=None:
            return left
        right=self.dfs2(original.right,cloned.right,target)
        return right
    
        