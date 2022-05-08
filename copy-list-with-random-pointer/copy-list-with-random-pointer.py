"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head==None:
            return None
        #hashmap implementation time complexity=O(n) and space=O(n)
        '''
        d={}
        temp=head
        while temp:
            d[temp]=Node(temp.val)
            temp=temp.next
        temp=head
        while temp:
            if temp.next==None:
                d[temp].next=None
            else:
                d[temp].next=d[temp.next]
            if temp.random==None:
                d[temp].random=None
            else:
                d[temp].random=d[temp.random]
            temp=temp.next
        return d[head]
    '''
        #time complexity=O(n) and space=O(1)
        temp=head
        #introducing duplicates nodes
        while temp!=None:
            newnode=Node(temp.val)
            newnode.next=temp.next
            temp.next=newnode
            temp=newnode.next
            
        temp=head
        #updating random pointer
        while temp!=None:
            if temp.random==None:
                temp.next.random=None
            else:
                temp.next.random=temp.random.next
            temp=temp.next.next
        
        #updating next pointer
        temp1,temp2=head,head.next
        result=head.next
        while temp1!=None:
            temp1.next=temp1.next.next
            if temp2.next==None:
                temp2.next=None
            else:
                temp2.next=temp2.next.next
            temp1=temp1.next
            temp2=temp2.next
        return result
    
    
            
        