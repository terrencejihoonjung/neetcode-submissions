class Solution {
    /**
     * @param {number[][]} intervals
     * @param {number[]} newInterval
     * @return {number[][]}
     */
    insert(intervals: number[][], newInterval: number[]): number[][] {
        const ret: number[][] = [];
        for (let i = 0; i < intervals.length; i++) {
            const [start, end] = intervals[i];

            if (end < newInterval[0]) ret.push([start, end]);
            else if (newInterval[1] < start) {
                return [...ret, newInterval, ...intervals.slice(i)];
            } else {
                newInterval = [Math.min(start, newInterval[0]), Math.max(end, newInterval[1])];
            }
        }

        ret.push(newInterval);
        return ret;
    }
}

// add intervals as long as end < newEnd 
// if newStart > end, add/return the newInterval and the rest of the intervals
// else, update newInterval by merging

// outside of the above loop, we just add the newInterval that was being updated 
// return