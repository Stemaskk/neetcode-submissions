class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set()
        for n in nums:
            numset.add(n)

        result = 0
        for n in numset:
            temp = 1
            if n - 1 not in numset:
                val = n
                while val + 1 in numset:
                    temp += 1 
                    val += 1
            if temp > result:
                result = temp

        return result