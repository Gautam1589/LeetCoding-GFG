class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        arr=[]
        for i in range(len(nums)):
            if nums[i]==1:
                arr.append(i)
                
        prefix_array=[0]*(len(arr)+1)
        prefix_array[0]=0
        print(arr)
        
        for i in range(1,len(arr)+1):
            prefix_array[i]=prefix_array[i-1]+arr[i-1]
        # print(prefix_array)
            
        i,j,ans=0,k-1,math.inf
        while j<len(arr):
            mid=i+(j-i)//2
            # print(mid)
            lsum=prefix_array[mid]-prefix_array[i]
            rsum=prefix_array[j+1]-prefix_array[mid+1]
            # print(lsum,rsum)
             
            if k&1:
                total=rsum-lsum
            else: 
                total=rsum-lsum-arr[mid]
            
            rad=mid-i
            if k&1:
                save=rad*(rad+1) 
            else:
                save=rad*(rad+1)+(rad+1)
            ans=min(ans,total-save)
            i+=1
            j+=1
            # print(ans)
        
        return ans