class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump = 0
        index = 0
        
        while maxJump < len(nums) - 1:

            maxJump = max(maxJump, nums[index] + index)

            index += 1

            if index > maxJump:
                return False

        return True