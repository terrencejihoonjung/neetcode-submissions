class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1: return 0
        list.sort(intervals)
        prevEnd = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            start,end = intervals[i]
            if prevEnd > start:
                prevEnd = min(prevEnd, end)
                res += 1
                continue
            
            prevEnd = end
        
        return res