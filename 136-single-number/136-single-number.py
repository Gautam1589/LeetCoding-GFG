class Solution:
    def singleNumber(self, nums: List[int]) -> int:
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
        