class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ""
        init = Counter(t)
        new = Counter()
        have, need = 0, len(init)
        start = 0
        num = float("inf")
        bstart, bend = 0, 0

        for i in range(len(s)):
            c = s[i]
            new[c] += 1
            if c in init and new[c] == init[c]:
                have += 1

            while have == need:
                if i - start + 1 < num:
                    num = i - start + 1
                    bstart, bend = start, i
                d = s[start]
                new[d] -= 1
                if d in init and new[d] < init[d]:
                    have -= 1
                start += 1

        if num == float("inf"):
            return ""
        return s[bstart : bend + 1]