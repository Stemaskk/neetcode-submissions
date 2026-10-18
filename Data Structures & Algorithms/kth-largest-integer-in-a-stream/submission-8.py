class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.nums = nums
        self.k = k
        
        if not nums:
            return None

        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]