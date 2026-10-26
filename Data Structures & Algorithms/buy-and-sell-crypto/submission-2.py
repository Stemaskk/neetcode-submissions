class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        start = 0
        maxProfit = 0

        for i in range(1, len(prices)):
            if prices[start] >= prices[i]:
                start = i

            maxProfit = max(maxProfit, prices[i] - prices[start])
        
        return maxProfit