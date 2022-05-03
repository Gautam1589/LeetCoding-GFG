class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start,end=len(nums),-1
        
        stack=[]
        for i in range(len(nums)):
            while stack and nums[stack[-1]]>nums[i]:
                start=min(start,stack.pop())
            stack.append(i)
        
        stack=[]
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]]<nums[i]:
                end=max(end,stack.pop())
            stack.append(i)
        
        if end==-1:
            return 0
        return end-start+1