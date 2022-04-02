class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        i = ptr = 0
        ans=0 

        while(ptr<len(nums)):
            if i%2==1:
                i+=1
            else:
                if ptr+1<len(nums) and nums[ptr]==nums[ptr+1]:
                    ans+=1
                    #dont change the index of the added things.
                else:
                    i+=1
            ptr+=1
        if i%2==1:
            return ans+1
        else:
            return ans  