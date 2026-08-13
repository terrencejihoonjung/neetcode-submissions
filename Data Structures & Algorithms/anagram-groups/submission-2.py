class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1: return [strs]

        anagrams = {}
        for str in strs:
            key = "".join(sorted(str))
            if key not in anagrams:
                anagrams[key] = [str]
            else:
                anagrams[key].append(str)
        
        return list(anagrams.values())

# group anagrams by a alphabetically sorted anagram key
# For each string, we will have to sort, so this algorithm runs in O(n * nlogn)
# edge cases include an strs of length 1 -> return [strs]

