class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0 for _ in range(len(temperatures))]
        
        for day,temp in enumerate(temperatures):
            while(stack != [] and stack[-1][1] < temp):
                p_day, p_temp = stack.pop()
                ans[p_day] = day - p_day
            stack.append((day,temp))
        return ans