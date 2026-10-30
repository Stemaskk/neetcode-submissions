class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        seen = set()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue 

            start = i + 1
            end = len(nums) - 1

            while start < end:
                if -(nums[start] + nums[end]) == nums[i]:
                    seen.add((nums[i], nums[start], nums[end]))
                    end -= 1
                    start += 1
                elif -(nums[start] + nums[end]) < nums[i]:
                    end -= 1
                else:
                    start += 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
            
        return [[i, j, k] for i, j, k in seen]