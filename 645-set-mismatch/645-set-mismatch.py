class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        
        ans=[]
        for i in d:
            if d[i]==2:
                ans.append(i)
                break
        
        for i in range(1,len(nums)+1):
            if i not in d:
                ans.append(i)
                return ans