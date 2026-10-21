class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        minTime = [float('inf')] * (n + 1)

        heap = [[0, k]]

        edges = {i : [] for i in range(n + 1)}
        for u, v, t in times:
            edges[u].append([v, t])

        minTime[k] = 0

        while heap:
            currTime, curr = heapq.heappop(heap)
            if currTime > minTime[curr]:
                continue
            for target, time in edges[curr]:
                newTime = currTime + time
                if newTime < minTime[target]:
                    minTime[target] = newTime
                    heapq.heappush(heap, (newTime, target))

        result = max(minTime[1:])
        if result == float('inf'):
            return -1
            
        return result