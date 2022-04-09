class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_i = []
        s_i[:] = s[::-1]
        if(len(s) == 0):
            return True
        for c in range(len(t)):
            if(s_i[-1] == t[c]):
                s_i.pop()
            if(not s_i):
                return True
        if(s_i):
            return False
        else:
            return True