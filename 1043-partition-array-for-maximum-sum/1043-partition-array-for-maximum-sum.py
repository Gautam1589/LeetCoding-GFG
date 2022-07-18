class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp=[0]*(len(arr))
        dp[0]=arr[0]
        
        for i in range(1,len(arr)):
            j=i
            max_,ans=0,0
            while j>=max(0,i-k+1):
                max_=max(max_,arr[j])
                if j>0:
                    ans=max(dp[i],dp[j-1]+(i-j+1)*max_)
                else:
                    ans=max(ans,max_*(i-j+1))
                dp[i]=ans
                j-=1
                          
        return dp[len(arr)-1]