class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) == 1 and len(s2) == 1: return s1 == s2

        dict = {}
        for c in s1: 
            if c not in dict: dict[c] = 1
            else: dict[c] += 1
        
        remaining = len(s1)

        left = 0
        for right in range(len(s2)):
            while left < right and (s2[right] not in dict or dict[s2[right]] == 0):
                if s2[left] in dict: 
                    dict[s2[left]] += 1
                    remaining += 1

                left += 1
            
            if s2[right] in dict:
                dict[s2[right]] -= 1
                remaining -= 1

            if remaining == 0: return True
        
        return False


# create a map out of s1 

# sliding window on s2
#   - keep moving right as long as we can "use up" a character in the map 
#   - if we can't use character (because c not in map or we ran out of c's), clean up + move left 

# how do we know whether we have a full permutation or not? 
#   - it would potentially take O(n) time to check each time 
#   - is there a O(1) way? -> track something in memory? 
#   - maybe track the # of characters used! 

# edge case:
#    - when s1 and s2 are length 1, check if they equal each other 