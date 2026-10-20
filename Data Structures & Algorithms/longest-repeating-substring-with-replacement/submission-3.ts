class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s: string, k: number): number {
        const freqs = new Map<string, number>();
        let maxFreq = 1;
        let ret = 1;

        let l = 0;
        for (let r = 0; r < s.length; r++) {
            freqs.set(s[r], ((freqs.get(s[r]) ?? 0) + 1));
            if (freqs.get(s[r]) > maxFreq) maxFreq = freqs.get(s[r]);

            while ((r - l + 1) - maxFreq > k) {
                freqs.set(s[l], freqs.get(s[l]) - 1);
                l++;
            }

            ret = Math.max(ret, r - l + 1);
        }
        return ret;
    }
}

// need to know the most frequently occurring letter in a given substring
// track most frequently occurring letter? -> map and a global variable
// calculate whether we ran out of k's to use? -> 
//      (length of window) - (most freq letter count) > k

// If we ran out of k's to use -> reset 
// WHILE calculation condition holds:
// 1. remove freq count for left pointer's letter 
// 2. move left pointer 

// each iteration (move right pointer)
// 1. update most freq letter count 
// 2. check whether we ran out of k's 
// 3. at this point we have a valid window so we record max length