# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.arr=[]
        self.inorder(root)
        return self.construct(0,len(self.arr)-1)
    
    def construct(self,beg,end):
        if beg>end:
            return None
        
        mid=(beg+end)//2
        root=TreeNode(self.arr[mid],None,None)
        
        root.left=self.construct(beg,mid-1)
        root.right=self.construct(mid+1,end)
        
        return root
        
    def inorder(self,root):
        if root==None:
            return 
        
        self.inorder(root.left)
        self.arr.append(root.val)
        self.inorder(root.right)
        
