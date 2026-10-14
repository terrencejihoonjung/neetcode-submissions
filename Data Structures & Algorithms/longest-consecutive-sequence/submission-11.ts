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
        const map = new Map<number, number>();
        for (let num of nums) {
            let count = 1;
            const originalNum = num;

            while (set.has(num + 1)) {
                if (map.has(num + 1)) {
                    count += map.get(num + 1);
                    break;
                }
                count++;
                
                num += 1;
            }

            map.set(originalNum, count);
            max = Math.max(max, count);
        }

        return max;
    }
}
