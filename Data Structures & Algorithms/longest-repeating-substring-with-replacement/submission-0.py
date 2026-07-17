class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict = {}
        max_freq = 0
        left = 0
        right = 0
        ans = 1

        while right < len(s):
            left_c = s[left]
            right_c = s[right]

            if right_c not in dict: dict[right_c] = 1
            else: dict[right_c] += 1

            max_freq = max(max_freq, dict[right_c])

            while (right - left + 1) - max_freq > k:
                dict[left_c] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
            right += 1
        
        return ans
        
# finding best window with k to replace letters
# keep iterating on A until we use up all of k
# once we hit the limit, we move the left pointer to the first occurrence of B
# how do we "reset" k without moving the right pointer so that we don't lose progress?

# break condition: lenght of window - count of most freq elem > k
# when we break, iterate left pointer and update map 

# when on ecah iteration calculate max length
