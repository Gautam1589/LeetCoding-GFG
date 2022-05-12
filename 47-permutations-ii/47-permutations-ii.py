class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        allsol=list()
        
        d=dict()
        for i in nums:
            d[i]=d.get(i,0)+1
            
        self.backtrack(nums,allsol,list(),d)
        return allsol
    
    def backtrack(self,nums,allsol,currsol,d):
        if len(currsol)==len(nums):
            allsol.append(currsol[:])
            return

        for i in d:
            if d[i]>0:
                currsol.append(i)
                d[i]-=1
                self.backtrack(nums,allsol,currsol,d)
                currsol.pop()
                d[i]+=1
            