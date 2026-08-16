class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in range(len(s2) - len(s1) + 1):
            window = s2[i:i + len(s1)]
            if self.isPermutation(window, s1): return True
        
        return False

    def isPermutation(self, w: str, s2: str) -> bool:
        freq = {}

        # get frequencies of w
        for c in w: 
            freq.setdefault(c, 0)
            freq[c] += 1

        # subtract frequencies in s2 
        for c in s2:
            if c not in freq: return False
            freq[c] -= 1

        # ensure all frequencies are 0 
        return all(val == 0 for val in freq.values())

# fixed-size window problem

# given s1 "abc", what makes s2 "___" a permutation of it?
#   - all letters in s2 must exist in s2
#   - all letters in s2 must occur the same # of times as those in s1 

# we can implement a function that checks whether a given window meets the above criteria 
# iterate through s2 using a fixed window == len(s1)
