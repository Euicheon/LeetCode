class Solution:
    def canJump(self, nums: List[int]) -> bool:
        tft = [0 for i in range(len(nums))]
        tft[0] = nums[0]
        if(len(nums) == 1): return True
        if(len(nums) == 2 and nums[0]>0): return True
        for i in range(1,len(nums)-1):
            if(tft[i-1] >= i):
                tft[i] = max(tft[i-1],nums[i]+i)
                # print(tft)
                if(tft[i] >= len(nums)-1): return True
        return False
