class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        #O(1) space
        x=0
        for i in nums:
            x^=i
        d=x&-x
        y1=0
        for i in nums:
            if i&d!=0:
                y1^=i
        y2=x^y1
        return [y1,y2]
    
        
        #O(N) time and O(N) space
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        
        res=[]
        for i in d:
            if d[i]==1:
                res.append(i)
        
        return res