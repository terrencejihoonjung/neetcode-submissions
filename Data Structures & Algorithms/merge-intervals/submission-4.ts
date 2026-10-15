class Solution {
    /**
     * @param {number[][]} intervals
     * @return {number[][]}
     */
    merge(intervals: number[][]): number[][] {
        if (intervals.length === 1) return intervals;

        intervals.sort((a, b) => a[0] - b[0])

        const stack: number[][] = [];
        for (const [start, end] of intervals) {
            if (stack.length > 0 && stack[stack.length - 1][1] >= start) {
                const [prevStart, prevEnd] = stack.pop();
                stack.push([Math.min(start, prevStart), Math.max(end, prevEnd)]);
            } else {
                stack.push([start, end]);
            }
        }

        return stack;
    }
}

// [1, 3], [4, 7], [2, 8] -> [1, 3], [2, 8], [4, 7] (sorted by start)

                            // [1, 3], [4, 7], [2, 8] (sorted by end)

// almost seems like it doesn't matter whether we sort by start or end -> either way makes it convenient 
// use stack that stores merged intervals 
// check top of stack with current interval to check if we have to merge 
// O(nlogn) time, O(n) space 
                        