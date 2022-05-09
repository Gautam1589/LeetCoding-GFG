class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #O(N) time with O(1) space
        i,l,r=0,0,len(nums)-1
        
        while i<=r:
            if nums[i]==0:
                nums[i],nums[l]=nums[l],nums[i]
                i+=1
                l+=1
            elif nums[i]==1:
                i+=1
            else:
                nums[i],nums[r]=nums[r],nums[i]
                r-=1
        
        #O(N)+O(N) time with O(1) space
        d={0:0,1:0,2:0}
        for i in nums:
            d[i]+=1
        k=0
        for i in d:
            for j in range(d[i]):
                nums[k]=i
                k+=1
            
        