class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify_max(nums)
        count = 0

        while count < k - 1:
            heapq.heappop_max(nums)
            count += 1
        
        return heapq.heappop(nums)