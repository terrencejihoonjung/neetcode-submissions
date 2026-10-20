class Solution {
    /**
     * @param {number[][]} intervals
     * @return {number[][]}
     */
    merge(intervals: number[][]): number[][] {
        const stack: number[][] = [];
        intervals.sort((a, b) => a[0] - b[0]); // sort start in asc order
        for (const interval of intervals) {
            if (stack.length > 0 && stack[stack.length - 1][1] >= interval[0]) {
                const [start, end] = stack.pop();
                stack.push([Math.min(start, interval[0]), Math.max(end, interval[1])]);
            } else {
                stack.push(interval);
            }
        }

        return stack;
    }
}

// build new list of merged intervals (stack)
// if the top element has overlap, pop -> merge -> add back to stack
// time/space -> O(n)