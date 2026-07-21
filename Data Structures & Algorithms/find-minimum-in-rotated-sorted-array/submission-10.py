class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        left = 0
        right = len(nums) - 1

        while left < right: 
            if nums[left] < nums[right]: return nums[left]

            mid = (left + right) // 2

            if nums[mid] >= nums[left]: left = mid + 1
            else: right = mid
        
        return nums[right]

# O(log n) time points to binary search

# start left pointer at 0 and right pointer at len(nums) - 1

# what do left and right tell us? 
#   - if left < right, then we have a monotonically increasing array, just return left's element
#   - else, we can assume that the min element is in the "right" section 

# what can we do with the middle element? 
#   - if the middle elemnet is greater than left, then we should update: left = mid + 1
#   - else, right = mid 

# return right's element at the end of the algorithm

# edge cases:
#   - when len(nums) == 1, return nums[0]