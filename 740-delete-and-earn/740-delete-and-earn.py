class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # [2|4] [3|9] [4|4] [5|10] [6|24]
        # max(4+f[2:],9+f[3:])
        memo = defaultdict(int)
        max_num = max(nums)
        for num in nums:
            memo[num] = num + memo[num]
            # max_num = max(max_num, num)
        @cache
        def max_f(num):
            if(num == 1):
                return memo[1]
            if(num == 0):
                return 0
            # print(num, max(memo[num]+max_f(num-1),memo[num-1]+max_f(num-2)))
            return max(memo[num]+max_f(num-2),max_f(num-1))
        return max_f(max_num)