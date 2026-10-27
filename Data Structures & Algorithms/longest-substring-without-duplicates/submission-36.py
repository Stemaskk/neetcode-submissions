class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = -1
        hashmap = dict()
        result = 0

        for right in range(len(s)):
            if s[right] in hashmap:
                left = max(left, hashmap[s[right]])

            hashmap[s[right]] = right


            result = max(result, right - left)

        return result