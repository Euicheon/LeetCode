class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split()
        for i in range(len(temp)):
            temp[i] = temp[i][::-1]
        ans = " ".join(temp)
        return ans