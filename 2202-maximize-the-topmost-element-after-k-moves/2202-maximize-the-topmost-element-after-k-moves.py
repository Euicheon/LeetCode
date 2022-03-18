class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if(len(nums) == 1 and k%2 == 1):
            return -1
        if(k == 1):
            return nums[1]
        if(k == 0):
            return nums[0]
        if(len(nums) == k):
            return max(nums[:k-1])
        elif(len(nums) > k):
            return max(max(nums[:k-1]),nums[k])
        else:
            return max(nums[:k+1])
        return 