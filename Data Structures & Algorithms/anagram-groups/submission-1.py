class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1: return [strs]

        anagrams = {}
        for str in strs:
            key = "".join(sorted(str))
            if key not in anagrams: anagrams[key] = [str]
            else: anagrams[key].append(str)
        
        return list(anagrams.values())