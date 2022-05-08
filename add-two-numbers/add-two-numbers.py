# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=None
        temp=head
        carry=0
        while l1!=None or l2!=None:
            if l1!=None:
                carry+=l1.val
                l1=l1.next
            if l2!=None:
                carry+=l2.val
                l2=l2.next
            if temp==None:
                temp=ListNode(carry%10)
                head=temp
            else:
                temp.next=ListNode(carry%10)
                temp=temp.next
            carry//=10
        if carry!=0:
            temp.next=ListNode(carry)
        return head
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        