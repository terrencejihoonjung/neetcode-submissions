class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
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
}

/* Brute Force
   - count frequencies of every unique number in nums 
   - sort the entries of the frequencies by the count 
   - return k entries' values 
   - time: O(nlogn), space: O(n) 
*/