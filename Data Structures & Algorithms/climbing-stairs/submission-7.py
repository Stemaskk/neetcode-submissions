class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        val1, val2 = 1, 2

        for i in range(3, n + 1):
            temp = val2
            val1 = val1 + val2
            val2 = val1
            val1 = temp

        return val2