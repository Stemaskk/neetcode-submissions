class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            currstone = heapq.heappop_max(stones)

            heapq.heapreplace_max(stones, abs(stones[0] - currstone))

        return stones[0]