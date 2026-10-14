class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s: string): number {
        if (s.length === 0) return 0;

        let max = 1
        let l = 0
        const set = new Set<string>()
        for (let r = 0; r < s.length; r++) {
            while (set.has(s[r])) {
                set.delete(s[l]);
                l++;
            }

            set.add(s[r])
            max = Math.max(max, r - l + 1)
        }

        return max
    }
}

// Build sliding window 
// - how to track unique characters? -> set since as soon as we hit at least 1 dupe, we hit the condition
// - move right pointer as long as we have unique characters in set 
// - if we hit a dupe, move left pointer once and remove from set 
// - at the end of each iteration, we record the current substring's length if larger than max