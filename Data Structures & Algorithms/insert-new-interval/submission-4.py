class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        newStart, newEnd = newInterval
        result = []
        added = False

        for start, end in intervals:
            if start <= newEnd and newStart <= end:
                newStart = min(start, newStart)
                newEnd = max(end, newEnd)
                continue
            
            if not added and newEnd < start:
                result.append([newStart, newEnd])
                added = True
            
            result.append([start, end])
        
        if not added:
            result.append([newStart, newEnd])

        return result
