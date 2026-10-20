class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number}
     */
    subarraySum(nums: number[], k: number): number {
        let ret = 0;
        let curr = 0;
        const map = new Map<number, number>();
        map.set(0, 1);

        for (const num of nums) {
            curr += num;
            const diff = curr - k;

            ret += map.get(diff) ?? 0;
            map.set(curr, (map.get(curr) ?? 0) + 1);
        }
        return ret;
    }
}