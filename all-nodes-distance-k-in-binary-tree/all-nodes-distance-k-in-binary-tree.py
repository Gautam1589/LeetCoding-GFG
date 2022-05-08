# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent={}
        self.cal_parent(root,parent)
    
        res=[]
        self.bfs(parent,target,k,res)
        return res
        
        
    def cal_parent(self,root,parent):
        queue=deque()
        queue.append(root)
        
        while queue:
            node=queue.popleft()
            
            if node.left:
                queue.append(node.left)
                parent[node.left]=node
            if node.right:
                queue.append(node.right)
                parent[node.right]=node
                
        return parent
    
    def bfs(self,parent,target,k,res):
        queue=deque()
        queue.append(target)
        vis={}
        vis[target]=1
        
        while queue:
            level=len(queue)
            
            if not k:
                break
            for i in range(level):
                node=queue.popleft()
                
                if node.left and node.left not in vis:
                    queue.append(node.left)
                    vis[node.left]=1
                if node.right and node.right not in vis:
                    queue.append(node.right)
                    vis[node.right]=1
                if node in parent and parent[node] not in vis:
                    queue.append(parent[node])
                    vis[parent[node]]=1
            
            k-=1
    
        while queue:
            res.append(queue.popleft().val)
            
        return res
                
                    
            
        
        
        
        
        
        
        
        
        
        