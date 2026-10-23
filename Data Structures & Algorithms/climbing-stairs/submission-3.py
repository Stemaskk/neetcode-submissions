class Solution:
    def climbStairs(self, n: int) -> int:
        
        var1, var2 = 1, 1

        for i in range(n - 1):
            temp = var1
            var1 = var1 + var2
            var2 = temp

        return var1