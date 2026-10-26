class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        leftstart = 0
        rightend = len(nums) - 1

        while leftstart <= rightend:
            middle = (leftstart + rightend) // 2
            if nums[middle] == target:
                leftend = middle - 1
                rightstart = middle + 1
                while leftstart <= leftend:
                    leftmiddle = (leftstart + leftend) // 2
                    if nums[leftmiddle] == target:
                        leftend = leftmiddle - 1
                    else:
                        leftstart = leftmiddle + 1

                while rightstart <= rightend:
                    rightmiddle = (rightstart + rightend) // 2
                    if nums[rightmiddle] == target:
                        rightstart = rightmiddle + 1
                    else:
                        rightend = rightmiddle - 1
                
                return [leftstart, rightend]

            elif nums[middle] > target:
                rightend = middle - 1

            else:
                leftstart = middle + 1

        return [-1, -1]