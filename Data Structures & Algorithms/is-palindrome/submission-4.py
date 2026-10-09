class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for c in s:
            if c.isalnum():
                clean += c.lower()

        for i in range(len(clean) // 2):
            if clean[i] != clean[len(clean) - i - 1]:
                return False
        
        return True