class Solution:
    def subCount(self,arr, n, k):
        # Your code goes here
        prefix=[0]*(n+1)
        
        for i in range(1,n+1):
            prefix[i]=prefix[i-1]+arr[i-1]
        #print(prefix)
        freq_rem={}
        for i in range(n+1):
            freq_rem[prefix[i]%k]=freq_rem.get(prefix[i]%k,0)+1
        #print(freq_rem)
        cnt=0
        for i in freq_rem:
            cnt+=(freq_rem[i]*(freq_rem[i]-1))//2
    
        return cnt
            

#{ 
#  Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        k=l[1]
        a = list(map(int,input().split()))
        ob = Solution()
        print(ob.subCount(a,n,k))
# } Driver Code Ends