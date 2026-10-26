class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        seen = defaultdict(int)
        seen[0] = 1
        count = 0
        total = 0

        for i in nums:
            total += i
            diff = total - k
            if diff in seen:
                count += seen[diff]
            seen[total] += 1

        return count