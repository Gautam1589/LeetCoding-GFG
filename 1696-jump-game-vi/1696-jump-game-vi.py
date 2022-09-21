class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n=len(nums)
        arr=[0]*n
        
        arr[0]=nums[0]
        heap=[]
        heappush(heap,(-nums[0],0))
        
        for i in range(1,n):
            while heap[0][1]<(i-k):
                heappop(heap)
            arr[i]=nums[i]+arr[heap[0][1]]
            heappush(heap,(-arr[i],i))
        
        return arr[n-1]