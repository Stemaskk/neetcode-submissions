class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end, middle = 0, len(nums) - 1, int(len(nums)/2)

        for i in range(len(nums)):
            if nums[start] == target:
                return start
            elif nums[middle] == target:
                return middle
            elif nums[end] == target:
                return end
            elif target  > nums[start] and target < nums[middle]:
                end = middle
                middle = int((end + start) / 2)
            elif target > nums[middle] and target < nums[end]:
                start = middle
                middle = int((end + start) / 2)

        return -1