# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k=len(lists)
        temp=head=None
        if k==0:
            return head
        h=[]
        for i in range(k):
            if lists[i]!=None:
                heappush(h,(lists[i].val,i))
            
        while h:
            v,p=heappop(h)
            if temp==None:
                temp=head=lists[p]
            else:
                temp.next=lists[p]
                temp=temp.next
            lists[p]=lists[p].next
            if lists[p]!=None:
                heappush(h,(lists[p].val,p))
        
        return head
            
            