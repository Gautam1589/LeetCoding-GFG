class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # even=[0]*len(arr)
        # odd=[0]*len(arr)

        even=0
        odd=0
        if arr[0]&1:
            odd=1
        else:
            even=1
        ans=odd
            
        for i in range(1,len(arr)):
            if arr[i]&1:
                odd,even=(even+1)%(10**9+7),odd%(10**9+7)
            else:
                even=(even+1)%(10**9+7)
            ans+=odd%(10**9+7)
            
        return ans%(10**9+7)
                