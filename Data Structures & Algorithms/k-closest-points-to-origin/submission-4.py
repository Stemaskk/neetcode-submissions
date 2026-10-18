class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        points = [[pow(x, 2) + pow(y, 2), x, y] for x, y in points]

        result = []

        while points:
            heapq.heappush_max(result, points[-1])
            if len(result) > k:
                heapq.heappop_max(result)
            points.pop()


        return [[x, y] for dist, x, y, in result]