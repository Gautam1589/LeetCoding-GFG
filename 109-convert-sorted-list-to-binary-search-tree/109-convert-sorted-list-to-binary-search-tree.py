# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums=[]
        while head:
            nums.append(head.val)
            head=head.next
        
        return self.construct(nums,0,len(nums)-1)
    
    def construct(self,nums,beg,end):
        if beg>end:
            return None
        
        mid=(beg+end)//2
        root=TreeNode(nums[mid],None,None)
        
        root.left=self.construct(nums,beg,mid-1)
        root.right=self.construct(nums,mid+1,end)
        
        return root