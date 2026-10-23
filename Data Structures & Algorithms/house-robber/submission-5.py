class Solution:
    def rob(self, nums: List[int]) -> int:
        
        """
        I think a brute force way of solving this problem is to probably iterate through each index, starting either from 0 or 1, since from index 2 we can reach them from index 0 or 1 so there is no reason to start there since we would miss out on index 0 or 1. Then we iterate through every possibilities of choosing, since we can choose indexs + 2 or higher, we do a check where it goes from all + 2 increments to +3, +4 etc. Then return the saved highest added values.

        That being said, we can solve this using dynamic programming, where like we said we can only start in index 0 or 1, we have index 3 which has the option to be jumped onto from these two indexs, and we update this index with a higher resulted sum. This will keep happening until the end of nums list, and we will return the highest value. We can keep track of this by making a constant variable.

        Index 2 is special, where it can only be jumped from index 0, so we will have a special case at the start for it to be updated properly, so we can use it for comparisons happening at index 4 and 5

        We could code this out by making an array that would hold these highest values, or update nums, we will update nums so it takes up less space

        """
        if len(nums) == 1:
            return nums[0]
            
        if len(nums) > 2:
            nums[2] += nums[0]

        for i in range(3, len(nums)):
            nums[i] += max(nums[i - 2], nums[i - 3])

        return max(nums[-1], nums[-2])





