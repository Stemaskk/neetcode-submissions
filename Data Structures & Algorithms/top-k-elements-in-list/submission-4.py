class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        topK = []
        count = defaultdict(int)
        result = []

        for i in range(len(nums)):
            count[nums[i]] += 1

        for num in count:
            heapq.heappush_max(topK, (count[num], num))

        for i in range(k):
            count, num = heapq.heappop_max(topK)
            result.append(num)

        return result