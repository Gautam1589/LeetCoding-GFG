# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        temp=head
        n=0
        while temp!=None:
            n+=1
            temp=temp.next

        n=n//2
        i=0
        temp=head
        while i<n:
            temp=temp.next
            i+=1
        print(temp.val)
        return temp
        '''
        slow,fast=head,head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow
        