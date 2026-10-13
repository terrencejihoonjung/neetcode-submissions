class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        if (s.length !== t.length) return false;

        const seen = new Map<string, number>()
        for (const c of s) {
            seen.set(c, (seen.get(c) ?? 0) + 1)
        }

        for (const c of t) {
            if (!seen.has(c)) return false;
            seen.set(c, seen.get(c) - 1)
        }

        for (const value of seen.values()) {
            if (value !== 0) return false
        }

        return true
    }
}
