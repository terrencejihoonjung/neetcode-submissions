class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums: number[]): number {
        if (nums.length === 0) return 0;

        const set = new Set<number>();
        for (const num of nums) set.add(num);

        let max = 1;
        for (let num of nums) {
            if (!set.has(num - 1)) {
                let len = 1;
                while (set.has(num + len)) {
                    len++;
                }
                max = Math.max(max, len)
            }
        }

        return max;
    }
}
