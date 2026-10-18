class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        used = set()

        def backtrack(array):
            if len(array) == len(nums):
                result.append(array[:])
                return 

            for i in range(len(nums)):
                if nums[i] not in used:
                    used.add(nums[i])
                    array.append(nums[i])
                    backtrack(array)
                    used.remove(nums[i])
                    array.pop()

        backtrack([])
        return result                