class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        temp = ''
        for i in range(len(s)):
            # print("------------",s[i])
            if s[i] in temp:
                temp = temp[temp.index(s[i])+1:] + s[i]
            else:
                temp += s[i]
            # print(temp, print(s[i]))
            ans = max(ans,len(temp))
        return ans