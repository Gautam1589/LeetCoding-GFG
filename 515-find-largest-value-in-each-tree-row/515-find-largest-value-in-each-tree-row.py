# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        return self.bfs(root)
    
    def bfs(self,root):
        if root==None:
            return []
        
        res=[]
        queue=deque()
        queue.append(root)
        while queue:
            level_size=len(queue)
            max_v=-math.inf
            for i in range(level_size):
                node=queue.popleft()
                max_v=max(max_v,node.val)
                
                if node.left!=None:
                    queue.append(node.left)
                if node.right!=None:
                    queue.append(node.right)

            res.append(max_v)
        return res
        