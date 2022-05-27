class Solution:
    def numberOfSteps(self, n: int) -> int:
        count=0
        while n:
            if n&1==0:
                n=n>>1
                count+=1
            else:
                n-=1
                count+=1
        return count
        