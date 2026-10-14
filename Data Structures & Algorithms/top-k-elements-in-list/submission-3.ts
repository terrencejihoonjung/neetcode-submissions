class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums: number[], k: number): number[] {
        const freqs = new Map<number, number>();
        for (const num of nums) {
            freqs.set(num, (freqs.get(num) ?? 0) + 1);
        }

        const buckets: number[][] = Array.from({length: nums.length + 1}, () => []);
        for (const [num, count] of freqs.entries()) {
            buckets[count].push(num);
        }

        const ans = new Array<number>();
        for (let i = buckets.length - 1; i >= 0; i--) {
            for (const num of buckets[i]) {
                ans.push(num);
                k--;
                if (k === 0) {
                    return ans
                }
            }
        }

        return ans
    }
}

/* Brute Force
   - count frequencies of every unique number in nums 
   - sort the entries of the frequencies by the count 
   - return k entries' values 
   - time: O(nlogn), space: O(n) 

   topKFrequent(nums: number[], k: number): number[] {
        const freqs = new Map<number, number>()
        for (const num of nums) {
            freqs.set(num, (freqs.get(num) ?? 0) + 1)
        }

        const entries = Array.from(freqs.entries())
        entries.sort((a, b) => b[1] - a[1])

        const ans = new Array<number>()
        for (let i = 0; i < k; i++) {
            ans.push(entries[i][0])
        }

        return ans
    }
*/

/* Optimization
   - count frequencies of every unique number in nums
   - create frequency "buckets" where bucket 0..n represents the frequency of a num in nums 
   - iterate backwards from the right-most bucket k times 
   - time: O(n), space: O(n)
*/