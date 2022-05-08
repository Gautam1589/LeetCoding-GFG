class MyHashSet:

    def __init__(self):
        self.hashset={}

    def add(self, key: int) -> None:
        self.hashset[key]=1

    def remove(self, key: int) -> None:
        if key in self.hashset:
            del self.hashset[key]

    def contains(self, key: int) -> bool:
        if key in self.hashset:
            return True
        return False

# class List:
#     def __init__(self,val):
#         self.next=None
#         self.val=val

# class MyHashSet:

#     def __init__(self):
#         self.head=None
#         self.temp=None

#     def add(self, key: int) -> None:
#         node=List(key)
#         if self.head==None:
#             self.head=node
#             self.temp=node
#         elif self.contains(key)==False:
#             self.temp.next=node
#             self.temp=self.temp.next

#     def remove(self, key: int) -> None:
#         if self.contains(key):
#             curr=self.head
#             while curr.next and curr.next.val!=key:
#                 curr=curr.next
#             if curr==self.head:
#                 self.head=None
#             else:
#                 curr.next=curr.next.next
    
#     def contains(self, key: int) -> bool:
#         curr=self.head
#         while curr:
#             if curr.val==key:
#                 return True
#             curr=curr.next
#         return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)