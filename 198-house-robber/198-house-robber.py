class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        
        dp_table = [-1 for _ in range(len(nums))]
        dp_table[-1], dp_table[-2] = nums[-1], max(nums[-2],nums[-1])
        for i in range(3,len(nums)+1):
            dp_table[-i] = max(dp_table[-i+1],dp_table[-i+2]+nums[-i])
        # print(dp_table)
        return dp_table[0]