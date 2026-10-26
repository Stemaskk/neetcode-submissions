class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        result = []  

        for i in range(len(nums) - 2):
            if nums[i] == nums[i - 1] and i != 0:
                continue
            goal = -(nums[i])

            start = i + 1
            end = len(nums) - 1

            while start < end:
                sum = nums[start] + nums[end]

                if sum == goal:
                    result.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                elif sum < goal:
                    start += 1
                else:
                    end -= 1

        return result
            


