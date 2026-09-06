class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans, length = "", float("inf")
        s_freq, t_freq = {}, {}

        for i in range(len(t)):
            t_freq.setdefault(t[i], 0)
            t_freq[t[i]] += 1
        
        l = 0
        have, need = 0, len(t_freq)
        for r in range(len(s)):
            s_freq.setdefault(s[r], 0)
            s_freq[s[r]] += 1

            if s[r] in t_freq and s_freq[s[r]] == t_freq[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < length:
                    ans = s[l: r + 1]
                    length = r - l + 1
                
                s_freq[s[l]] -= 1
                
                if s[l] in t_freq and s_freq[s[l]] < t_freq[s[l]]:
                    have -= 1
                
                l += 1

        return ans

# brute force:
# create a map using t (for check whether a letter in s is in t)

# gather all substrings in s that include every letter in t
#   - as soon as a valid substring is found update left pointer
#   - when a letter in s is in t, begin substring building 
#       - keep going until all of t is matched or we exhaust 
#       - if we get a match AND its shorter length, update min substring

# if min substring lenght is 0, return ""

# 