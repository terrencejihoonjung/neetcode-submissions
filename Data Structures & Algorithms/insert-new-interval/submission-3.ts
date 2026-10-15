class Solution {
    /**
     * @param {number[][]} intervals
     * @param {number[]} newInterval
     * @return {number[][]}
     */
    insert(intervals: number[][], newInterval: number[]): number[][] {
        if (intervals.length === 0) return [newInterval];

        const result: number[][] = [];
        for (let i = 0; i < intervals.length; i++) {
            const [start, end] = intervals[i];

            if (end < newInterval[0]) {
                result.push([start, end]);
            }

            else if (newInterval[1] < start) {
                result.push(newInterval, ...intervals.slice(i))
                return result;
            }

            else {
                newInterval = [Math.min(newInterval[0], start), Math.max(newInterval[1], end)];
                continue;
            }
        }

        result.push(newInterval);
        return result;



        // Add all intervals where end is less than start of newInterval 

        // Check 3 scenarios: reached end, start is greater than newInterval's end (insert), overlap

        // If we find overlap, we then solve the merge intervals problem from there 
    }
}

// Iteratively build new list of intervals 
// At each iteration I check: 
// - overlap with current interval? -> merge
// - overlap with next interval? -> merge
// - no overlap and fits in between current and next? -> insert 
// - else -> add current interval and continue 