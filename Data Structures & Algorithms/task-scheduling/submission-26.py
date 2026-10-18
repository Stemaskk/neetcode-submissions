class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = defaultdict(int)

        for t in tasks:
            count[t] += 1
        
        numCount = [0] * (len(tasks) + 1)
        maxCount = 0

        for c in count.values():
            numCount[c] += 1
            maxCount = max(c, maxCount)
        
        total = (maxCount - 1) * (n + 1) + numCount[maxCount]
        
        return max(total, len(tasks))
