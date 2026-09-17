"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0: return 0
        if len(intervals) == 1: return 1

        starts = [interval.start for interval in intervals]
        ends = [interval.end for interval in intervals]
        
        list.sort(starts)
        list.sort(ends)

        s = 0
        e = 0
        count = 0
        res = 0
        while s < len(starts):
            if starts[s] < ends[e]:
                count += 1
                s += 1
            
            else:
                count -= 1
                e += 1
            res = max(count, res)
            
        return res