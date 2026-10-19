class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        result = []

        def backtrack(index, array):

            if index == len(nums):
                result.append(array[:])
                return
            
            array.append(nums[index])
            backtrack(index + 1, array)
            array.pop()

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1

            backtrack(index + 1, array)


        backtrack(0, [])

        return result