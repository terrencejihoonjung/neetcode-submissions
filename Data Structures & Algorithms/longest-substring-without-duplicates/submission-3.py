class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0

        seen = set()
        left = 0
        ans = 1

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                            
            seen.add(s[right])
            ans = max(ans, right - left + 1)
        
        return ans
                
                
                


# sliding window algorithm 
# keep moving right pointer until we find a character that already exists in the window 

# how do we know the condition breaks? we can't just rely on the left pointer 
# use a set that reflects the unique characters in the window ?
#   - if the next element is in the set, we move the left pointer until we reach it -> clean up 

# O(n) space, O(n) time on avg 