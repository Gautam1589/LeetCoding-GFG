class Solution:
    def longestPalindrome(self, s: str) -> str:
        #return self.manachers_algo(s)
    
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
                    
        return s[start:end+1]
    
    
    def manachers_algo(self,s):
        n=len(s)
        ns=['']*(2*n+1)
        p=[-1]*(2*n+1)
        j=0
        ns[j]='#'
        j+=1
        for i in range(n):
            ns[j]=s[i]
            j+=1
            ns[j]='#'
            j+=1
        
        c,r=0,0
        lc,ll=0,0
        
        for i in range(len(ns)):
            m=2*c-i
            if r>i:
                p[i]=min(p[m],r-i)
            
            a=i+p[i]+1
            b=i-p[i]+1
            while b>=0 and a<len(ns) and ns[a]==ns[b]:
                b-=1
                a+=1
                p[c]+=1
                
            if p[i]>=ll:
                ll=p[i]
                lc=i
            if i+p[i]>r:
                c=i
                r=i+p[i]
        
        for i in range(len(p)):
            if p[i]=='#':
                p[i]=''
                
        return ''.join(p)
        
        
    
#             n = len(s)
            
#             dp = [[False]*len(s) for i in range(n)]
            
#             l,r = 0,0
#             for x in range(n):
#                 i = 0
#                 j = x
#                 while j<n-x:
#                     if i == j:
#                         dp[i][j] = True
#                     elif s[i] == s[j]:
#                         if x == 1:
#                             dp[i][j] = True
#                         else:
#                             dp[i][j] = dp[i+1][j-1]
#                     else:
#                         dp[i][j] = False
#                     if dp[i][j]:
#                         l,r = i,j
#                     i += 1
#                     j += 1
#             return s[l:r+1]