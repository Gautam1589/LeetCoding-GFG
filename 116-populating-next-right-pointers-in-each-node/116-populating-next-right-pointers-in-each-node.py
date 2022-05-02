"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root==None:
            return None
        
        queue=[]
        queue.append(root)
        
        while queue:
            level=len(queue)
            
            for i in range(level-1):
                queue[i].next=queue[i+1]
            
            for i in range(level):
                node=queue.pop(0)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        return root