class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right, result = [], [], []
        prodl, prodr = 1, 1
        size = len(nums) - 1
        for n in range(len(nums)):
            prodl *= nums[n]
            prodr *= nums[size - n]
            left.append(prodl)
            right.append(prodr)
            
        right.reverse()

        result.append(right[1])
        for n in range(1, size):
            result.append(left[n - 1] * right[n + 1])

        result.append(left[size - 1])
        return result