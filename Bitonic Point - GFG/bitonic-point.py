#User function Template for python3
class Solution:

	def findMaximum(self,arr, n):
		# code here
		beg,end=0,n-1
		
		while beg<=end:
		    mid=(beg+end)//2
		    if (mid==0 or arr[mid]>arr[mid-1]) and (mid==n-1 or arr[mid]>arr[mid+1]):
		        return arr[mid]
		    else:
		        if arr[mid]<arr[mid+1]:
		            beg=mid+1
		        else:
		            end=mid-1

#{ 
#  Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends