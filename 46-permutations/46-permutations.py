class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        allsol=list()
        self.backtrack(nums,allsol,list(),dict())
        
        return allsol
    
    def backtrack(self,nums,allsol,currsol,vis):
        if len(currsol)==len(nums):
            allsol.append(currsol[:])
            return
        
        for i in range(len(nums)):
            if nums[i] not in vis:
                currsol.append(nums[i])
                vis[nums[i]]=1
                print(vis)
                self.backtrack(nums,allsol,currsol,vis)
                currsol.pop()
                del vis[nums[i]]