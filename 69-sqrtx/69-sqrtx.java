class Solution:
    def mySqrt(self, x: int) -> int:
        #O(logn)
        if x==0:
            return 0
        i,j=1,x
        mid=1
        while i<j:
            mid=(i+j)//2
            if mid*mid==x or i+1==j:
                break
            else:
                if mid*mid<x:
                    i=mid
                else:
                    j=mid       
        return mid
        
        
        # O(N)
        if x==0:
            return 0
        for i in range(1,x//2+2):
            if i*i==x:
                return i
            elif i*i>x:
                return i-1