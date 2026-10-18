class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            currstone = heapq.heappop_max(stones)

            stones[0] = abs(stones[0] - currstone)
            heapq.heapify_max(stones)

        return stones[0]