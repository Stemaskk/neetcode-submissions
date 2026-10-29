class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        charCount = defaultdict(int)

        maxFrequency = 0
        left = 0
        result = 0

        for right in range(len(s)):
            charCount[s[right]] += 1
            maxFrequency = max(maxFrequency, charCount[s[right]])

            while (right - left + 1) - maxFrequency > k:
                charCount[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result








