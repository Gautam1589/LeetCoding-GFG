class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #O(mn) time, O(mn) space
        return self.table(word1,word2) 
        
        #O(mn) time, O(mn) space, extra stack space -O(m+n) or max(m,n)
        dp={}
        return self.memoise(word1,word2,len(word1),len(word2),dp)
    
    def memoise(self,s1,s2,m,n,dp):
        if m==0:
            dp[(m,n)]=n
            return n
        if n==0:
            dp[(m,n)]=m
            return m
        if (m,n) in dp:
            return dp[(m,n)]
        
        if s1[m-1]==s2[n-1]:
            dp[(m,n)]=self.memoise(s1,s2,m-1,n-1,dp)
        else:
            dp[(m,n)]=1+min(self.memoise(s1,s2,m-1,n,dp),self.memoise(s1,s2,m,n-1,dp))
        
        return dp[(m,n)]
    
    def table(self,word1,word2):
        m=len(word1)
        n=len(word2)
        dp=[[0]*(n+1) for i in range(m+1)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        
        return m-dp[m][n]+n-dp[m][n]