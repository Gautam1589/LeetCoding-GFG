# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    global paths
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root,p,q) #O(N)-time O(1)-space
        
        # self.paths=[]
        # self.dfs2(root,p,[]) #O(N+N)-time O(logn+logn)-space
        # print(self.paths)
        # path2=self.dfs2(root,q,[])
        # #print(path1,path2)
        # for i in path1[::-1]:
        #     for j in path2[::-1]:
        #         if i.val==j.val:
        #             return i
        
        
    def dfs(self,root,p,q):
        if root==None:
            return None
        
        if root.val==p.val or root.val==q.val:
            return root
        
        left=self.dfs(root.left,p,q)
        right=self.dfs(root.right,p,q)
        
        if left!=None and right!=None:
            return root
        if left!=None:
            return left
        else:
            return right
        
#     def dfs2(self,root,target,path):
#         if root==None:
#             return
        
#         if root.left==None and root.right==None and root.val==target.val:
#             path.append(root.val)
#             self.paths.append(path[:])
#             return        
        
#         path.append(root.val)
#         self.dfs2(root.left,target,path)
#         self.dfs2(root.left,target,path)
#         path.pop()
        