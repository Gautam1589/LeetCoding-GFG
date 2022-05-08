class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        if n==0:
            return False
        if n & (n-1)==0 and (str(bin(n)).count('0')-1)%2==0:
            return True
        return False
        