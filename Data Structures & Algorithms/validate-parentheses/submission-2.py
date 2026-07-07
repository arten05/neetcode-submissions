class Solution:
    def isValid(self, s: str) -> bool:
        res = [s[0]]
        for i in range(1, len(s)):
            if len(res) == 0:
                res.append(s[i])
            elif res[-1] + s[i] in ('()', '{}', '[]'):
                res.pop()
            
            else:
                res += s[i]
        return len(res) == 0
        