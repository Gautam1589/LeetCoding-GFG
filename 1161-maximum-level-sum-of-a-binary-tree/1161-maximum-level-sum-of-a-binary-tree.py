# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        return self.bfs(root)
    
    def bfs(self,root):
        res=[]
        queue=deque()
        queue.append(root)
        max_sum=-math.inf
        level=1
        while queue:
            level_size=len(queue)
            curr_sum=0
            for i in range(level_size):
                node=queue.popleft()
                curr_sum+=node.val
                
                if node.left!=None:
                    queue.append(node.left)
                if node.right!=None:
                    queue.append(node.right)
                    
            if curr_sum>max_sum:
                max_sum=curr_sum
                max_level=level
                
            level+=1
        return max_level