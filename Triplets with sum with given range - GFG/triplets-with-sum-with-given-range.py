#User function Template for python3

class Solution:
    def countTriplets(self, Arr, N, L, R):
        # code here
        Arr.sort()
        return self.find_count(Arr,N,R)-self.find_count(Arr,N,L-1)
        
    def find_count(self,arr,n,target):
        count=0
        for i in range(n-2):
            low=i+1
            high=n-1
            while low<high:
                if arr[i]+arr[low]+arr[high]>target:
                    high-=1
                else:
                    count+=(high-low)
                    low+=1
        return count

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        L,R = input().split()
        L=int(L)
        R=int(R)
        ob = Solution()
        print(ob.countTriplets(Arr, N, L, R))
# } Driver Code Ends