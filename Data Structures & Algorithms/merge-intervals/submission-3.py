class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1: return intervals 

        # sort by start
        sorted_intervals = sorted(intervals)

        stack = [sorted_intervals[0]]
        for i in range(1, len(sorted_intervals)):
            prev = stack[-1]
            curr = sorted_intervals[i]

            if curr[0] <= prev[1]:
                popped = stack.pop()
                stack.append([min(popped[0], curr[0]), max(popped[1], curr[1])])
            else:
                stack.append(curr)
        
        return stack
            