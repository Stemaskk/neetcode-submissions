class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        minheap = [[0, points[0][0], points[0][1]]]
        visited = set()

        total = 0

        while len(visited) < len(points):
            dist, currX, currY = heapq.heappop(minheap)
            if (currX, currY) in visited:
                continue
            visited.add((currX, currY))
            total += dist
            for X, Y in points:
                if (X, Y) not in visited:
                    dist = abs(currX - X) + abs(currY - Y)
                    heapq.heappush(minheap, [dist, X, Y])

        return total