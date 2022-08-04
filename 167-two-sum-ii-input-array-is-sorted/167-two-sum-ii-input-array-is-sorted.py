class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #return self.recursive(0,len(numbers)-1,target,numbers)
        #return self.optimize(0,len(numbers)-1,target,numbers)
        #return self.memoise(0,len(numbers)-1,target,numbers,{})
        return self.two_pointer(0,len(numbers)-1,target,numbers)
        
    #O(N) time O(1) space
    def two_pointer(self,i,j,target,numbers):    
        while i<j:
            s = numbers[i] + numbers[j]
            if s == target:
                return [i + 1 , j + 1]
            
            if s > target:
                j-=1
            else:
                i+=1 
        return []
        
    #O(2^N) time O(1) space O(N) stack space
    def recursive(self,i,j,target,numbers):
        if i==j:
            return [-1,-1]
        
        if numbers[i]+numbers[j]==target:
            return [i+1,j+1]
        
        ans=self.recursive(i+1,j,target,numbers)
        if ans[0]!=-1:
            return ans
        return self.recursive(i,j-1,target,numbers)
    
    #O(N^2) time O(N^2) space O(N) stack space
    def memoise(self,i,j,target,numbers,dp):
        if (i,j) in dp:
            return dp[(i,j)]
        
        if i==j:
            dp[(i,j)]=[-1,-1]
            return [-1,-1]
        
        if numbers[i]+numbers[j]==target:
            dp[(i,j)]=[i+1,j+1]
            return [i+1,j+1]
        
        ans=self.memoise(i+1,j,target,numbers,dp)
        if ans[0]!=-1:
            dp[(i,j)]=ans
            return ans
        dp[(i,j)]=self.memoise(i,j-1,target,numbers,dp)
        return dp[(i,j)]
    
    #O(N) time O(1) space O(N) stack space
    def optimize(self,i,j,target,numbers):
        if i==j:
            return [-1,-1]
        
        if numbers[i]+numbers[j]==target:
            return [i+1,j+1]
        
        if numbers[i]+numbers[j]<target:
            return self.recursive(i+1,j,target,numbers)
        else:
            return self.recursive(i,j-1,target,numbers)
    