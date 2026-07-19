class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        if len(s) == 1: return 1

        seen = set() 
        left = 0
        right = 0
        max_len = 1
        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
            right += 1
        
        return max_len

        
# sliding window of unque characters 
# move right pointer until we hit a dupe
# while left pointer is a dupe, remove from dict and move forward 