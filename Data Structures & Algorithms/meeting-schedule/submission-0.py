"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        a=sorted(intervals,key=lambda x:x.start)
        for i in range(0,len(a)-1):
            if a[i].end>a[i+1].start:
                return False
        return True