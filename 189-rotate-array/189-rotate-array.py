class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        t = k%l
        if(l==1 or t==0):
            return nums
        nums[:] = nums[-t:] + nums[:l-t]
        # print(nums)
        