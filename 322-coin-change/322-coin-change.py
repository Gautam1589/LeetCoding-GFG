class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp={}
        # res=self.memoise(coins,len(coins),amount,dp)
        # if res==int(10e9):
        #     return -1
        # else:
        #     return res
        return self.table(coins,len(coins),amount)
    
    
    def memoise(self,s,m,n,dp):
        if n==0:
            dp[(m,n)]=0
            return dp[(m,n)]
        
        if m==0:
            dp[(m,n)]=int(10e9)
            return dp[(m,n)]
         
        if (m,n) in dp:
            return dp[(m,n)]
            
        if s[m-1]>n:
            dp[(m,n)]=0+self.memoise(s,m-1,n,dp)
            return dp[(m,n)]
        
        dp[(m,n)]=min(0+self.memoise(s,m-1,n,dp),1+self.memoise(s,m,n-s[m-1],dp))
        return dp[(m,n)]
    
    def table(self,s,m,n):
        dp=[[int(10e9)]*(n+1) for i in range(m+1)]
        
        for i in range(m+1):
            dp[i][0]=0
            
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]>j:
                    dp[i][j]=0+dp[i-1][j]
                else:
                    dp[i][j]=min(0+dp[i-1][j],1+dp[i][j-s[i-1]])
                    
        if dp[m][n]==int(10e9):
            return -1
        else:
            return dp[m][n]
        