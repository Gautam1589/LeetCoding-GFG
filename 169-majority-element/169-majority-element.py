class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #O(Nlogn) time #O(1) space
        N=len(nums)
        nums.sort()
        cnt=0
        ele = nums[N//2]
        for i in nums:
            if i==ele:
                cnt+=1
        return ele if cnt>N//2 else -1

        #hash map
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        
        n=len(nums)//2
        for i in d:
            if d[i]>n:
                return i
            
        #Moore algorithm
        c=1
        m=nums[0]
        for i in nums:
            if i==m:
                c+=1
            else:
                c-=1
            if c==0:
                m=i
                c=1
        cnt=0
        for i in nums:
            if i==m:
                cnt+=1
        return m if cnt>len(nums)//2 else -1
        