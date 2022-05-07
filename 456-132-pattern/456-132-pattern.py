class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        return self.solve1(nums)
        #return self.solve2(nums)
        #return self.solve3(nums)
    
    #O(N) time with O(2N) space
    def solve1(self,nums):
        n=len(nums)
        min_arr=[]
        min_arr.append(nums[0])
        for i in range(1,n):
            min_arr.append(min(min_arr[i-1],nums[i]))
        
        stack=[]
        for j in range(n-1,-1,-1):
            while stack and stack[-1]<=min_arr[j]:
                stack.pop()
            if stack and nums[j]>stack[-1]:
                return True
            stack.append(nums[j])
        return False
    
    #O(N^3) time with O(1) space
    def solve2(self,nums):
        n=len(nums)
        
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    if nums[i]<nums[k]<nums[j]:
                        return True
        return False
    
    #O(N^2) time with O(1) space
    def solve3(self,nums):
        n=len(nums)
        
        min_ele=math.inf
        for j in range(n-1):
            min_ele=min(min_ele,nums[j])
            
            if nums[j]<=min_ele:
                continue
            
            for k in range(j+1,n):
                if min_ele<nums[k]<nums[j]:
                    return True
        return False