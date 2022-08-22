class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg=0
        j=0
        while j<k:
            max_avg+=nums[j]
            j+=1
        
        curr=max_avg
        max_avg/=k
        
        i=1
        while j<len(nums):
            curr-=nums[i-1]
            curr+=nums[j]
            
            max_avg=max(max_avg,curr/k)
            i+=1
            j+=1
        return max_avg