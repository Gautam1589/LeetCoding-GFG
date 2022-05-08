# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return None
        res=[]
        queue=deque()
        queue.append(root)
        while queue:
            level_size=len(queue)
            for i in range(level_size):
                node=queue.popleft()
                if i==level_size-1:
                    res.append(node.val)
                if node.left!=None:
                    queue.append(node.left)
                if node.right!=None:
                    queue.append(node.right)
        
        return res