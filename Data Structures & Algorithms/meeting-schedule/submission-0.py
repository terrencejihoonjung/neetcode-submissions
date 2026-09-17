"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0 or len(intervals) == 1: return True

        # sort metings by start 
        list.sort(intervals, key=lambda item:item.start)
        # if a overlap is found return false, return true at the end 
        for i in range(1, len(intervals)):
            prev = intervals[i - 1]
            curr = intervals[i]

            if prev.end > curr.start: return False
        
        return True
        