class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        seen = set()

        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1

            while start < end:
                if -(nums[start] + nums[end]) == nums[i]:
                    array = [nums[i], nums[start], nums[end]]
                    seen.add(tuple(sorted(array)))
                    end -= 1
                    start += 1
                elif -(nums[start] + nums[end]) < nums[i]:
                    end -= 1
                else:
                    start += 1
            
        return [[i, j, k] for i, j, k in seen]