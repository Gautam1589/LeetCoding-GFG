# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lis=[]
        if root==None:
            return lis
        
        q=[]
        q.append(root)
        while q:
            n=len(q)
            l=[]
            while n:
                node=q.pop(0)
                l.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                n-=1
            lis.append(l)
        return lis
                
                
            
            
        