# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        return self.level_order_traversal(root)
    
    def level_order_traversal(self,root):
        if root==None:
            return None
        
        queue=deque()
        queue.append(root)
        
        while queue:
            l=len(queue)
            
            sum_=0
            for i in range(l):
                node=queue.popleft()
                sum_+=node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return sum_
        