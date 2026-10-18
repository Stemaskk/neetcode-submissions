class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []

        def backtrack(index, array, total):
            if total >= target or index == len(nums):
                if total == target:
                    result.append(array[:])
                return
            array.append(nums[index])
            backtrack(index, array, total + nums[index])
            array.pop()
            backtrack(index + 1, array, total)

        backtrack(0, [], 0)

        return result