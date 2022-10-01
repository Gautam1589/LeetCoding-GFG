class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        ans=[]
        for i in arr:
            ans.append([i,abs(x-i)])
        
        ans.sort(key=lambda x:x[1])
        res=[]
        
        for i in range(k):
            res.append(ans[i][0])
        
        res.sort()
        return res