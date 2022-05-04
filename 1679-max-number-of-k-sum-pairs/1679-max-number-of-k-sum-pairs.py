class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        
        cnt=0
        for i in d:
            if k-i in d:
                if not k&1 and i==k//2:
                    cnt+=d[i]//2
                else:
                    cnt+=min(d[i],d[k-i])
                    d[i]=max(d[i]-cnt,0)
                    d[k-i]=max(d[k-i]-cnt,0)
    
        return cnt 
        
#         memory limit exceeded
#         arr=[0]*(10**9)
#         for i in nums:
#             arr[i]+=1
        
#         i,j=1,10**9-1
#         cnt=0
#         while i<j:
#             if nums[i]!=0 and nums[j]!=0:
#                 cnt+=min(nums[i],nums[j])
#             i+=1
#             j-=1
        
#         cnt+=nums[0]//2
#         cnt+=nums[i]//2
#         return cnt