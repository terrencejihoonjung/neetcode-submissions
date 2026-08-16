class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # build a map of s1 frequencies and record remaining letters
        freq = {} 
        for c in s1: 
            freq.setdefault(c, 0)
            freq[c] += 1
        
        remaining = len(s1)

        # use sliding window algorithm 
        left = 0
        for right in range(len(s2)):
            # while the right pointer is not in map OR we ran out of the right's letter, 
            # move left and update the map and remaining and update left. 
            while left < right and (s2[right] not in freq or freq[s2[right]] == 0): 
                if s2[left] in freq: 
                    freq[s2[left]] += 1
                    remaining += 1
                left += 1
            
            # update map and remaining 
            if s2[right] in freq:
                freq[s2[right]] -= 1
                remaining -= 1

            # check if remaining is 0
            if remaining == 0: return True
        
        return False

# OPTIMIZATION: 
# Can we improve this to be O(n) time and O(1) memory?

# think using a fixed window would complicate this and restrict us actually. 
# let's just build a window 
# if we EVER encounter a letter that is not in s1 OR we an out of that letter, we should reset the window by iterating the left and resetting the map 
# we can track the letters remaining to use up within a window so we can guarantee that we've used up all available letters in s1. When remaining == 0, we have a valid permutation 


# BRUTE FORCE:
# O(nm) time and O(n) memory

# fixed-size window problem

# given s1 "abc", what makes s2 "___" a permutation of it?
#   - all letters in s2 must exist in s1
#   - all letters in s2 must occur the same # of times as those in s1 

# we can implement a function that checks whether a given window meets the above criteria 
# iterate through s2 using a fixed window == len(s1)
