# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr=self.inorder(root,[])
        self.i=-1
        
    def inorder(self,root,l):
        if root==None:
            return
        
        self.inorder(root.left,l)
        l.append(root.val)
        self.inorder(root.right,l)
        
        return l
            
    def next(self) -> int:
        self.i+=1
        return self.arr[self.i]

    def hasNext(self) -> bool:
        if self.i==len(self.arr)-1:
            return False
        return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()