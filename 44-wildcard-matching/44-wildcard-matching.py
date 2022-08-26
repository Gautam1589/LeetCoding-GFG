class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m=len(p)
        n=len(s)
        if m==0 and n==0:
            return True
        elif m==0 and n!=0:
            return False
        
        dp=[[False]*(n+1) for i in range(m+1)]
        
        dp[m][n]=True
        if p[m-1]=='*':
            dp[m-1][n]=True
        for i in range(m-2,-1,-1):
            if p[i]=='*':
                dp[i][n]=dp[i+1][n]
        
        for i in range(m-1,-1,-1):
            flag=dp[i+1][n]
            for j in range(n-1,-1,-1):
                if p[i]==s[j] or p[i]=='?':
                    dp[i][j]=dp[i+1][j+1]
                elif p[i]=='*':
                    flag=flag or dp[i+1][j]
                    if flag==True:
                        dp[i][j]=True
                    else:
                        dp[i][j]=False
        return dp[0][0]
    
                     
                