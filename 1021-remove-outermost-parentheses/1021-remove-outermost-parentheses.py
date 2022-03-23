class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        temp = 0
        rmvList = []
        for i,p in enumerate(s):
            if (temp == 0 and p is '('):
                temp += 1
                rmvList.append(i)
            elif p is '(':
                temp += 1
            elif p is ')' and temp == 1:
                temp -= 1
                rmvList.append(i)
            elif p is ')':
                temp -= 1
        
        s = ''.join(s[x] for x in range(len(s)) if x not in rmvList)
        return s