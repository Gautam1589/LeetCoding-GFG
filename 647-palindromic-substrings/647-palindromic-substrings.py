class Solution:
    def countSubstrings(self, s: str) -> int:
        start,end=-1,-1
        dp=[[False]*len(s) for i in range(len(s))]
        for gap in range(len(s)):
            i,j=0,gap
            while j<len(s):
                if gap==0:
                    dp[i][j]=True
                    start,end=i,j
                elif gap==1 and s[i]==s[j]:
                    dp[i][j]=True
                    start,end=i,j
                elif s[i]==s[j] and dp[i+1][j-1]==True:
                    dp[i][j]=True
                    start,end=i,j
                j+=1
                i+=1
                    
        cnt=0
        for i in range(len(s)):
            for j in range(len(s)):
                if dp[i][j]:
                    cnt+=1
        return cnt