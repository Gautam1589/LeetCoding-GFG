class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp1={}
        dp2={}
        return self.foo(0,dp1,dp2,prices)
    
    def foo(self,i,dp1,dp2,prices):
        if i in dp1:
            return dp1[i]
        
        if i==len(prices):
            dp1[i]=0
            return 0
        
        notbuy=self.foo(i+1,dp1,dp2,prices)
        buy=self.g(i+1,dp1,dp2,prices)-prices[i]
        dp1[i]=max(notbuy,buy)
        return dp1[i]
    
    def g(self,i,dp1,dp2,prices):
        if i in dp2:
            return dp2[i]
        
        if i==len(prices):
            dp2[i]=prices[len(prices)-1]
            return dp2[i]
        
        dp2[i]=max(self.g(i+1,dp1,dp2,prices),prices[i]+self.foo(i+1,dp1,dp2,prices))
        return dp2[i]