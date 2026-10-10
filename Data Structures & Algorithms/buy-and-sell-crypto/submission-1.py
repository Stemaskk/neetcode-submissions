class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        total = 0

        for i in prices:
            minprice = min(minprice, i)
            total = max(i - minprice, total)
        
        return total