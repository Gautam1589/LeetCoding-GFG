#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        return self.solve1(n,arr,dep)
    
    def solve1(self,n,arr,dep):
        l=[]
        for i in range(n):
            l.append([arr[i],'a'])
            l.append([dep[i],'d'])
        
        l.sort()
        ans=[0]*(len(l)+1)
        for i in range(1,len(l)+1):
            if l[i-1][1]=='a':
                ans[i]=ans[i-1]+1
            else:
                ans[i]=ans[i-1]-1
        return max(ans)
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends