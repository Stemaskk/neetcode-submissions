class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        result = 0
        for n in numset:
            temp = 1
            if n - 1 not in numset:
                val = n
                while val + 1 in numset:
                    temp += 1 
                    val += 1
            result = max(result, temp)

        return result