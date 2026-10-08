class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += str(len(s)) + "*" + s
        return output

    def decode(self, s: str) -> List[str]:
        input = []
        strlen = ""
        i = 0
        while i < len(s):
            if s[i] != '*':
                strlen += s[i]
                i += 1
            elif s[i] == "*":
                i += 1
                input.append(s[i : i + int(strlen)])
                i += int(strlen)
                strlen = ""
        return input
