class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1: return 1

        dict = {}
        max_freq = 0
        left = 0
        ans = 1

        for right in range(len(s)):
            if s[right] not in dict: dict[s[right]] = 1
            else: dict[s[right]] += 1

            max_freq = max(max_freq, dict[s[right]])

            while (right - left + 1) - max_freq > k:
                dict[s[left]] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)

        return ans


# sliding window problem, move right pointer until what? 
# until we hit the limit for k

# track # of most frequent element in window 

# how do we know when we can or cannot use k? 
# we cannot use k when the length - # of most frequent element > k
# else we can just move the right pointer 

# in breaking condition, we need to clean up
# how do we know when to subtract from most_freq? 
#   - use a dictionary to remove the freq of the left pointer's element first 
#   

# order of operations
# 1. update dictionary with right pointer
# 2. update max_freq = max(max_freq, dict[right])
# 3. while (breaking condition), dict[left] -= 1 and left += 1
# 4. 