class Solution {
    /**
     * @param {number[][]} intervals
     * @param {number[]} newInterval
     * @return {number[][]}
     */
    insert(intervals: number[][], newInterval: number[]): number[][] {
        if (intervals.length === 0) return [newInterval];

        const ret: number[][] = [];
        for (let i = 0; i < intervals.length; i++) {
            const [start, end] = intervals[i];

            if (end < newInterval[0]) {
                ret.push([start, end]);
            }

            else if (start > newInterval[1]) {
                return [...ret, newInterval, ...intervals.slice(i)];
            }

            else {
                newInterval = [Math.min(newInterval[0], start), Math.max(newInterval[1], end)];
            }
        }

        ret.push(newInterval);
        return ret;
    }
}

// if end is < newInterval's start, then we add interval
// if start > newInterval's end, we add the newInterval and the rest of the intervals 
// the remaining cases are overlap or add newInterval at the end 
// - if overlap, merge newInterval with current interval and add newInterval to the end 