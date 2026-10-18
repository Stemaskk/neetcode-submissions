class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        heap = [c for c in count.values()]

        heapq.heapify_max(heap)
        cycle = 0

        cooldown = deque()

        while heap or cooldown:
            cycle += 1

            if heap:
                remaining = heapq.heappop_max(heap) - 1
                if remaining != 0:
                    cooldown.append((remaining, cycle + n))
            else:
                cycle = cooldown[0][1]

            if cooldown and cooldown[0][1] == cycle:
                heapq.heappush_max(heap, cooldown.popleft()[0])

        return cycle
