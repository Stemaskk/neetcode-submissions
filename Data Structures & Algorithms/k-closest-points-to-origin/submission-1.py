class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        points = [[pow(x, 2) + pow(y, 2), x, y] for x, y in points]

        heapq.heapify_max(points)

        while len(points) > k:
            heapq.heappop_max(points)

        points = [[x, y] for dist, x, y, in points]

        return points