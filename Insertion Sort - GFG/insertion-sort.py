#Sort the array using insertion sort

class Solution:
    def insert(self, alist, index, n):
        #code here
        i=index-1
        x=alist[index]
        while i>=0 and x<alist[i]:
            alist[i+1]=alist[i]
            i-=1
    
        alist[i+1]=x
        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        #code here
        for j in range(1,n):
            self.insert(alist,j,n)

#{ 
#  Driver Code Starts
if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
    
        Solution().insertionSort(arr,n)
    
        for i in range(n):
            print(arr[i],end=" ")
    
        print()
# } Driver Code Ends