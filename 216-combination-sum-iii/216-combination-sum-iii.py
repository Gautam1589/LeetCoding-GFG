class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums=[1,2,3,4,5,6,7,8,9]
        allsol=[]
        self.backtrack(nums,n,k,0,allsol,[])
        return allsol
    
    def backtrack(self,nums,n,k,i,allsol,currsol):
        if sum(currsol)==n and len(currsol)==k:
            allsol.append(currsol[:])
            return
        
        if i==len(nums):
            return
        
        sol1=copy.deepcopy(currsol)
        sol2=copy.deepcopy(currsol)
        sol1.append(nums[i])
        self.backtrack(nums,n,k,i+1,allsol,sol1)
        self.backtrack(nums,n,k,i+1,allsol,sol2)
