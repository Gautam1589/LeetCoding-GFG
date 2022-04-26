# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        return self.bfs(root)
    
    def bfs(self,root):
        if root==None:
            return 0
        
        res=[]
        queue=deque()
        queue.append(root)
        while queue:
            level_size=len(queue)
            avg=0
            for i in range(level_size):
                node=queue.popleft()
                avg+=node.val
                
                if node.left!=None:
                    queue.append(node.left)
                if node.right!=None:
                    queue.append(node.right)
            avg=avg/level_size
            res.append(avg)
        return res