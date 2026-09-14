class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start 
        intervals = sorted(intervals, key=lambda item: item[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            start,end = res[-1]
            if intervals[i][0] <= end:
                popped = res.pop()
                res.append([min(popped[0], intervals[i][0]), max(popped[1], intervals[i][1])])
            else:
                res.append(intervals[i])
            
        return res
