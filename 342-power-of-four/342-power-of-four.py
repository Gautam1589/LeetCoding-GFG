class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return self.solve(n,0)
    
    def solve(self,n,x):
        if 4**x==n:
            return True
        elif 4**x>n:
            return False
        
        return self.solve(n,x+1)
    