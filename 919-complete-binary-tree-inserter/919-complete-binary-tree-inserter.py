# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
#O(n^2) time
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root_=root

    #O(n) time
    def insert(self, val: int) -> int:
        newnode=TreeNode(val)
        queue=deque()
        queue.append(self.root_)
        
        while queue:
            node=queue.popleft()
            if node.left==None:
                node.left=newnode
                return node.val
            else:
                queue.append(node.left)
            
            if node.right==None:
                node.right=newnode
                return node.val
            else:
                queue.append(node.right)

    def get_root(self) -> Optional[TreeNode]:
        return self.root_


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()