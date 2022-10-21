class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        even=[0]*len(arr)
        odd=[0]*len(arr)
        if arr[0]&1:
            odd[0]=1
        else:
            even[0]=1
            
        for i in range(1,len(arr)):
            if arr[i]&1:
                odd[i]=even[i-1]+1
                even[i]=odd[i-1]
            else:
                even[i]=even[i-1]+1
                odd[i]=odd[i-1]
                
        return sum(odd)%(10**9+7)
                