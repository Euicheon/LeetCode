class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [inf for i in range(len(nums))]
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(i+1,min(i+1+nums[i],len(nums))):
                dp[j] = min(dp[j],dp[i]+1)
            # print(dp)
        return dp[-1]