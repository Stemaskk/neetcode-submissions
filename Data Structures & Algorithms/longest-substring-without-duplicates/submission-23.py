class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = dict()
        result = 0
        reset = 0

        for i in range(len(s)):
            if s[i] in substr and reset <= substr[s[i]]:
                reset = substr[s[i]] + 1
            substr[s[i]] = i
            result = max(result, i - reset + 1)

        return result