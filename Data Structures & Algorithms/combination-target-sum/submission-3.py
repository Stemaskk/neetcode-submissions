class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []

        def backtrack(index, array):
            total = sum(array)
            if total >= target or index == len(nums):
                if total == target:
                    result.append(array[:])
                return
            array.append(nums[index])
            backtrack(index, array)
            array.pop()
            backtrack(index + 1, array)

        backtrack(0, [])

        return result