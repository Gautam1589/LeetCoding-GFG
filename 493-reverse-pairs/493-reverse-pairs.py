class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        #O(Nlogn)+O(N)+O(N)
        self.cnt=0
        self.mergesort(nums,0,len(nums))
        return self.cnt
        
        #O(N^2)
        cnt=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i]>2*nums[j]:
                    cnt+=1
        return cnt
    
    def mergesort(self,nums,p,r):
        if p<r-1:
            q=(p+r)//2
            self.mergesort(nums,p,q)
            self.mergesort(nums,q,r)
            self.merge(nums,p,q,r)
            
    def merge(self,nums,p,q,r):
        l=nums[p:q]
        r=nums[q:r]
            
        #counting reverse pairs
        j=0
        for i in range(len(l)):
            while j<len(r) and l[i]>2*r[j]:
                j+=1
            self.cnt+=j

        #TLE
        # for j in range(len(r)):
        #     for i in range(len(l)):
        #         if l[i]>2*r[j]:
        #             self.cnt+=(len(l)-i)
        #             break
        
        #merging
        i,j,k=0,0,p
        while i<len(l) and j<len(r):
            if l[i]<=r[j]:
                nums[k]=l[i]
                i+=1
            else:
                nums[k]=r[j]
                j+=1
            k+=1
        while i<len(l):
            nums[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            nums[k]=r[j]
            j+=1
            k+=1
        