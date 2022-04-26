# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        return self.bfs(root)
    
    def bfs(self,root):
        queue=deque()
        queue.append(root)
        nonleaf=True
        while queue:
            node=queue.popleft()
            
            if nonleaf==False and (node.left or node.right):
                return False
            if node.left==None and node.right!=None:
                return False
            if (node.left==None and node.right==None) or (node.left!=None and node.right==None):
                nonleaf=False
            
            if node.left!=None:
                queue.append(node.left)
            if node.right!=None:
                queue.append(node.right)
    
        return True
        