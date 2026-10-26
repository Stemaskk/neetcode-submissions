class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        match = {'(' : ')', '[' : ']', '{' : '}'}

        for i in range(len(s)):
            if s[i] in match:
                stack.append(s[i])

            else:
                if not stack:
                    return False

                if match[stack[-1]] == s[i]:
                    stack.pop()

                else:
                    return False

        if not stack:
            return True

        return False