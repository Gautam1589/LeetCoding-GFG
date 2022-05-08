# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return None
        
        queue=deque()
        queue.append(root)
        ans=[]
        
        level=1
        while queue:
            level_size=len(queue)
            
            curr=[]
            for i in range(level_size):
                if level&1:
                    node=queue.popleft()
                else:
                    node=queue.pop()
                
                curr.append(node.val)
                if level&1:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)
            ans.append(curr)
            level+=1
        
        return ans
                    