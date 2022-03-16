class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        temp = 0
        for c in s:
            if c == "(":
                temp += 1
            if c == ")":
                temp -= 1
            ans = max(temp,ans)
        print(ans)
        return ans
    