class Solution:
    def maxArea(self, heights: List[int]) -> int:
        val = 0
        start = 0
        end = len(heights) - 1
        while start < end: 
            val = max((end - start) * min(heights[start], heights[end]), val)
            if heights[start] > heights[end]:
                end -= 1
            else:
                start += 1

        return val