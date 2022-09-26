class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        f_max=-math.inf
        s_max=-math.inf
        t_max=-math.inf
        
        nums=set(nums)
        for i in nums:
            if i>f_max:
                t_max=s_max
                s_max=f_max
                f_max=i
            elif i>s_max:
                t_max=s_max
                s_max=i
            elif i>t_max:
                t_max=i
        
        return f_max if len(nums)<=2 else t_max
        