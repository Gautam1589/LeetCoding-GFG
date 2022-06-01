class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res=x^y
        cnt=0
        while res:
            if res&1:
                cnt+=1
            res>>=1
        return cnt