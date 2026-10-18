"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        if len(intervals) == 1:
            return 1
        rooms = 1
        intervals.sort(key=lambda x: x.start)
        min_time = []

        if intervals[0].end > intervals[1].start:
            rooms += 1
            heapq.heappush(min_time, intervals[0].end)
            heapq.heappush(min_time, intervals[1].end)
        else:
            heapq.heappush(min_time, intervals[1].end)

        for i in range(2, len(intervals)):
            min_start = heapq.heappop(min_time)
            if intervals[i].start < min_start:
                rooms += 1
                heapq.heappush(min_time, min_start)
            heapq.heappush(min_time, intervals[i].end)
        
        return rooms