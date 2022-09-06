class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return max(self.solve(len(nums),1,nums,{},0),self.solve(len(nums)-1,0,nums,{},0))
    
    def solve(self,n,m,nums,dp,money):
        if (money,n) in dp:
            return dp[(money,n)]
        
        if n<=m:
            dp[(money,n)]=money
            return money
        
        dp[(money,n)]=max(self.solve(n-2,m,nums,dp,money+nums[n-1]),self.solve(n-1,m,nums,dp,money))
        return dp[(money,n)]