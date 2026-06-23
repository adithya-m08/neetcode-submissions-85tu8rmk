"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        minh=[]
        intervals.sort(key=lambda x: x.start)

        for interval in intervals:
            if minh and minh[0]<=interval.start:
                heapq.heappop(minh)
            heapq.heappush(minh, interval.end)
        return len(minh)