class Solution:
    def firstUniqChar(self, s: str) -> int:

        count = defaultdict(int)
        
        for char in s:
            count[char] += 1
        
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
            
        return -1