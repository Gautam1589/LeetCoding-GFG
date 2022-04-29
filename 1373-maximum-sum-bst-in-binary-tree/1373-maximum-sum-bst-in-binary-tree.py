# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Node:
    def __init__(self, sum_=0, min_=math.inf, max_=-math.inf):
        self.sum_=sum_ 
        self.min_=min_
        self.max_=max_
        
class Solution:
    global curr_sum,max_sum
        
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        #O(N)
        self.max_sum=0
        self.solve2(root)
        return self.max_sum
        
        
        #O(N^2)
        self.max_sum=0
        self.solve1(root)
        return self.max_sum
    
    def solve2(self,root):
        if root==None:
            return Node()
        
        left_node=self.solve2(root.left)
        right_node=self.solve2(root.right)
        
        if not left_node or not right_node:
            return None
        
        if root.val<=left_node.max_ or root.val>=right_node.min_:
            return None
        
        self.curr_sum=left_node.sum_+right_node.sum_+root.val
        self.max_sum=max(self.max_sum,self.curr_sum)
        
        return Node(self.curr_sum,min(left_node.min_,root.val),max(right_node.max_,root.val))
    
    def solve1(self,root):
        if root==None:
            return
        
        self.solve1(root.left)
    
        self.curr_sum=0
        if self.validate(root,-math.inf,math.inf):
            self.max_sum=max(self.max_sum,self.curr_sum)

        self.solve1(root.right)
        
    def validate(self,root,ll,ul):
        if root==None:
            return True
        
        if root.val>ll and root.val<ul:
            self.curr_sum+=root.val
            return self.validate(root.left,ll,root.val) and self.validate(root.right,root.val,ul)
        
        return False