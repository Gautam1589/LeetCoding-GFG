class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        d={}
        for i in arr:
            d[i]=d.get(i,0)+1
            
        i=1
        while k>0:
            if i in d:
                i+=1
                continue
            k-=1
            i+=1
            
        return i-1