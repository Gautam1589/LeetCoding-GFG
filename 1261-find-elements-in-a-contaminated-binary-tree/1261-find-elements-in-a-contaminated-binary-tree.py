# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val=0
        self.map=set()
        self.recover(root)
        
    def recover(self,root_):
        if root_==None:
            return None
        
        self.map.add(root_.val)
        
        if root_.left:
            root_.left.val=2*root_.val+1
            self.recover(root_.left)
        if root_.right:
            root_.right.val=2*root_.val+2
            self.recover(root_.right)
        
    def find(self, target: int) -> bool:
        return target in self.map


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)