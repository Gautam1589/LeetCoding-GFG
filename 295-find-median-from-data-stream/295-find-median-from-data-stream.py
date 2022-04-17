from heapq import *
class MedianFinder:

    def __init__(self):
        self.max_heap=[]
        self.min_heap=[]
        self.med=0

    def addNum(self, num: int) -> None:
        if len(self.max_heap)==0 and len(self.min_heap)==0:
            self.med=num
            heappush(self.max_heap,-num)
        else:    
            if num<=self.med:
                if len(self.max_heap)>len(self.min_heap):
                    heappush(self.min_heap,-heappop(self.max_heap))
                heappush(self.max_heap,-num)
            else:
                if len(self.min_heap)>len(self.max_heap):
                    heappush(self.max_heap,-heappop(self.min_heap))
                heappush(self.min_heap,num)
            self.findMedian()
            
    def findMedian(self) -> float:
        if len(self.max_heap)>len(self.min_heap):
            self.med=-self.max_heap[0]
        elif len(self.min_heap)>len(self.max_heap):
            self.med=self.min_heap[0]
        else:
            self.med=(-self.max_heap[0]+self.min_heap[0])/2
        
        return self.med


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()