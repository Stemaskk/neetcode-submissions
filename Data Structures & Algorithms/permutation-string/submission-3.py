class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        value = Counter(s1)
        size = len(s1)

        for i in range(len(s2) - size + 1):
            count = Counter()
            for j in range(i, i + size): 
                count[s2[j]] += 1
            if value == count:
                return True

        return False