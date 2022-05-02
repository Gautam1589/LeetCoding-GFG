# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue=[]
        queue.append(root)
        
        while queue:
            level=len(queue)
            ans=queue[0].val
            
            flag=0
            for i in range(level):
                node=queue.pop(0)
                
                if node.left:
                    queue.append(node.left)
                    flag=1
                if node.right:
                    queue.append(node.right)
                    flag=1
            
            if flag==0:
                return ans