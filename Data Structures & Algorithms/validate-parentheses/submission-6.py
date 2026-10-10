class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        for i in range(len(s)):
            if s[i] == '[' or s[i] == '{' or s[i] == '(':
                result.append(s[i])
            elif result and ((s[i] == ']' and result[-1] == '[') or
                             (s[i] == '}' and result[-1] == '{') or
                             (s[i] == ')' and result[-1] == '(')):
                result.pop()
            else:
                return False
        return not result