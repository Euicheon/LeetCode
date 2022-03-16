class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        target = tickets[k]
        for i in tickets[:k+1]:
            ans += min(i,target)
        for j in tickets[k+1:]:
            ans += min(j,target-1)
        return ans