class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i,j=0,1
        while j<len(nums):
            if nums[i]&1:
                if nums[j]&1:
                    j+=1
                else:
                    nums[i],nums[j]=nums[j],nums[i]
                    i+=1
                    j+=1
            else:
                i+=1
                j+=1
                
        return nums