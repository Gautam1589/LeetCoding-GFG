class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #3rd
        nums.sort()
        for i in range(len(nums)):
            if nums[i]!=i:
                return i
        
        #2nd
        for i in range(len(nums)+1):
            nums.append(i)
    
        res=0
        for i in nums:
            res^=i
        return res
        
        #1st
        s=sum(nums)
        n=len(nums)
        l=n*(n+1)//2
        return l-s
    
    