# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue=deque()
        queue.append(root)
        
        while queue:
            level=len(queue)
            
            flag1=0
            for i in range(level):
                node=queue.popleft()
                
                if node.val==x or node.val==y:
                    flag1+=1
                
                flag2=0
                if node.left:
                    if node.left.val in (x,y):
                        flag2+=1
                    queue.append(node.left)
                if node.right:
                    if node.right.val in (x,y):
                        flag2+=1
                    queue.append(node.right)
                if flag2==2:
                    return False
        
            if flag1==1:
                return False
        return True