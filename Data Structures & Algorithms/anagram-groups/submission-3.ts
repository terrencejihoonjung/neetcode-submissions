class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {
        const anagrams = new Map<string, string[]>()
        for (const str of strs) {
            const sorted = str.split("").sort().join("")
            if (!anagrams.has(sorted)) {
                anagrams.set(sorted, [str])
            } else {
                anagrams.get(sorted).push(str)
            }
        }

        return Array.from(anagrams.values())
    }
}
