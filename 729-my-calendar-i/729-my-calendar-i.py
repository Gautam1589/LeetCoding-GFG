class MyCalendar:

    def __init__(self):
        self.event=[]
        self.event.append([-1,-1])
        self.event.append([10**9+1,10**9+1])

    def book(self, start: int, end: int) -> bool:
        self.event.sort()
        i=1
        while i<len(self.event):
            if end<=self.event[i][0] and start>=self.event[i-1][1]:
                self.event.insert(-2,[start,end])
                return True
            i+=1
             
        #print(self.event)
        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)