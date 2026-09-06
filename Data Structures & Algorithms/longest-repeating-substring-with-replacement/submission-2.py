class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1: return 1

        ans = 1
        freq = {}
        most_freq = 1
        l = 0
        n = len(s)

        for r in range(n):
            freq.setdefault(s[r], 0)
            freq[s[r]] += 1
            
            most_freq = max(most_freq, freq[s[r]])

            while (r - l + 1) - most_freq > k:
                freq[s[l]] -= 1
                l += 1
            
            ans = max(ans, r - l + 1) 
        
        return ans
            


# using the available "k" is easy, the tricky part is the cleanup
# while (window length - most_frequent  < k):
#   - update frequency of left pointer's element
#   - recover a switch (k) 
#   - move left pointer forward

# we'll need a way to distinguish which elements we didn't switch and switched 
# -> track the most frequent element

# do we need to know the most frequent element or just the count value?
#   - use a map that represents frequency of elements in the window 
#   - we need the map to keep track of the most frequent element's count 
