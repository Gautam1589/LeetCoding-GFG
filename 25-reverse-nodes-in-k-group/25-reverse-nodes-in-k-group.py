# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(-1,None)
        dummy.next=head
        prev=dummy
        curr,next_=None,None
        
        n=0
        temp=head
        while temp:
            n+=1
            temp=temp.next
    
        while n>=k:
            curr=prev.next
            next_=curr.next
            
            for i in range(1,k):
                curr.next=next_.next
                next_.next=prev.next
                prev.next=next_
                next_=curr.next
            prev=curr
            n-=k
        
        return dummy.next