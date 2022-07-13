class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #O(Nlogn)+O(logn) time
        def predicate(mid,nums):
            if (mid<0 or nums[mid-1]!=nums[mid]) and (mid>=len(nums) or nums[mid]!=nums[mid+1]):
                return True
            else:
                if mid&1:
                    return nums[mid-1]!=nums[mid]
                else:
                    return nums[mid]!=nums[mid+1]
                
        nums.sort()
        beg,end=0,len(nums)-1
        while beg<end:
            mid=(beg+end)//2
            if predicate(mid,nums):
                end=mid
            else:
                beg=mid+1
        return nums[beg]
        
        #O(N) time O(N) space
        vis=[0]*max(nums)
        for i in nums:
            if vis[i]==0:
                vis[i]+=1
            else:
                vis[i]-=1
        for i in vis:
            if i==1:
                return i
            
        #O(N) time O(N) space
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        for i in d:
            if d[i]==1:
                return i
            
        #O(N)
        res=0
        for i in nums:
            res^=i
            
        return res
        