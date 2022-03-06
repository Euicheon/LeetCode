class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums) == 1:
            return [nums]
        for i in range(len(nums)):
            temp = nums.copy()
            # print(nums,i)
            temp.pop(i)
            tempList = self.permute(temp)
            for j in tempList:
                ans.append(j+[nums[i]])
        return ans