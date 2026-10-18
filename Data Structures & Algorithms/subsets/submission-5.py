class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(index, array):

            if index == len(nums):
                result.append(array[:])
                return
            
            backtrack(index + 1, array)
            array.append(nums[index])
            backtrack(index + 1, array)
            array.pop()


        backtrack(0, [])

        return result
