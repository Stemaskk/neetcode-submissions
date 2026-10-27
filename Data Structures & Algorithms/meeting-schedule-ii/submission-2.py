"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key=lambda x : x.start)

        endHeap = []

        for interval in intervals:
            if endHeap and interval.start >= endHeap[0]:
                heapq.heappop(endHeap)
            
            heapq.heappush(endHeap, interval.end)
                
        return len(endHeap)