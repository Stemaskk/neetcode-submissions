class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        result = [intervals[0]]

        for i in range(1, len(intervals)):

            currStart, currEnd = intervals[i]
            prevStart, prevEnd = result[-1]


            if (currStart >= prevStart and currStart <= prevEnd) or (currEnd >= prevStart and currEnd <= prevEnd):
                
                result[-1][0] = min(result[-1][0], currStart)
                result[-1][1] = max(result[-1][1], currEnd)
                
            else:
                result.append([currStart, currEnd])
            
        return result