class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #1st
        for i in range(len(nums)+1):
            nums.append(i)
    
        res=0
        for i in nums:
            res^=i
        return res
        
        #2nd
        s=sum(nums)
        n=len(nums)
        l=n*(n+1)//2
        return l-s
    
    