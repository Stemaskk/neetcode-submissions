class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        result = ""

        for i in range(len(min(strs))):
            curr = strs[0][i]
            for s in strs:
                if s[i] != curr:
                    return result
            result += curr

        return result

