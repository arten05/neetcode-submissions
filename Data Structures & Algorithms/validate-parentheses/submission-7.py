class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for i in range(len(s)):
            if len(res) == 0:
                res.append(s[i])
            elif res[-1] + s[i] in ('()', '{}', '[]'):
                res.pop()
            
            else:
                res += s[i]
        return len(res) == 0
        