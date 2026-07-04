class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums: 
            seen.add(num)
        
        len_max = 0
        for num in nums:
            curr = num
            while curr - 1 in seen: curr -= 1

            temp = 1
            while curr + 1 in seen: 
                temp += 1
                curr += 1
            len_max = max(len_max, temp)
            if len_max >= (len(nums) // 2): return len_max

        return len_max
                    
                    
# add all nums to set
# iterate through nums and if num is in set we start a search
# in a search, we check backwards in case a num exists
# then start search -> record max length 
# if the length is greater than or equal to half the list, we early return