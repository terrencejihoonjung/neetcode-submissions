class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        s_freq, t_freq = {}, {}

        for c in t: 
            t_freq.setdefault(c, 0)
            t_freq[c] += 1
        
        have, need = 0, len(t_freq)
        ret = ""
        ret_length = float("inf")

        l = 0
        for r in range(n):
            c = s[r]
            # update s_freq
            s_freq.setdefault(c, 0)
            s_freq[c] += 1

            # if updating s_freq leads to a requirement on t_freq being met -> udpate have
            if c in t_freq and t_freq[c] == s_freq[c]:
                have += 1

            # if all requirements are met
            while have == need:
                if (r - l + 1) < ret_length: 
                    ret = s[l:r + 1]
                    ret_length = r - l + 1
                
                s_freq[s[l]] -= 1

                if s[l] in t_freq and s_freq[s[l]] < t_freq[s[l]]:
                    have -= 1
                
                l += 1
        
        return ret


# using have and need to keep track of whether we met the requirements for the substring and t
#   - includes keeping track of frequencies in the window as well as a separate fixed map for t

# when requirements are met, we can clean up from the left pointer
#   - if requirements still met, just update the ret IF it has a smaller substring length
#   - if requirements not met anymore, we need to update have -> continue right pointer