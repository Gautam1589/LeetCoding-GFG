class NumArray:

    def __init__(self, nums: List[int]):
        self.__nums=nums
        self.__prefix=self.pre_calculation()
    
    def pre_calculation(self):
        arr=[0]*(len(self.__nums)+1)
        
        for i in range(1,len(self.__nums)+1):
            arr[i]=arr[i-1]+self.__nums[i-1]
        return arr

    def sumRange(self, left: int, right: int) -> int:
        return self.__prefix[right+1]-self.__prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)