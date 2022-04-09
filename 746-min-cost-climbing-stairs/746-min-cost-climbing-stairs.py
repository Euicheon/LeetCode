class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        temp = [0 for i in range(len(cost)+1)]
        temp[0] = 0
        temp[1] = 0
        for i in range(2,len(cost)+1):
            # print(cost[i-1],temp[i-1],cost[i-2],temp[i-2])
            temp[i] = min(cost[i-1]+temp[i-1],cost[i-2]+temp[i-2])
        return temp[-1]
