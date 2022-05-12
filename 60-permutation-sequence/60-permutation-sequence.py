class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums=[]
        for i in range(1,n+1):
            nums.append(i)
            
        while k-1:
            nums=self.next_permutation(nums)
            k-=1
            
        nums=[str(i) for i in nums]
        return ''.join(nums)
            
    def next_permutation(self,nums):
        for k in range(len(nums)-2,-1,-1):
            if nums[k]<nums[k+1]:
                break
        else:
            nums.sort()
            return nums
                
        for l in range(len(nums)-1,k,-1):
            if nums[l]>nums[k]:
                nums[l],nums[k]=nums[k],nums[l]
                break
                
        i,j=k+1,len(nums)-1
        while i<j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
        
        return nums