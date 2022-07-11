class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i,j=0,0
        n=len(nums)
        res=[]
        queue=deque()
        while j<n:
            while len(queue)>0 and nums[j]>queue[-1]:
                queue.pop()
            queue.append(nums[j])
            
            if j-i+1==k:
                i+=1
                res.append(queue[0])
                if queue[0]==nums[i-1]:
                    queue.popleft()
            j+=1
            
        return res