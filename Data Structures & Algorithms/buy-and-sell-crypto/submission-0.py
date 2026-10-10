class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        total = 0

        for i in range(1, len(prices)):
            minprice = min(minprice, prices[i])
            total = max(prices[i] - minprice, total)
        
        return total