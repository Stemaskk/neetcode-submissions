class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
    
        end = len(cost)

        if end <= 2:
            return min(cost[0], cost[1])
        if end == 3:
            return min(cost[0] + cost[2], cost[1])

        for i in range(2, end):
            cost[i] += min(cost[i - 1], cost[i - 2])

        return min(cost[-1], cost[-2])
