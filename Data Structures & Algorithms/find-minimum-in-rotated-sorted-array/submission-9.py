class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        # use binary search on nums to find the drop/min element in the middle
        left = 0 
        right = len(nums) - 1
        while left < right:
            if nums[left] < nums[right]:
                return nums[left]
            
            mid = (left + right) // 2

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
            
        return nums[right]



# we can eliminate monotonically increasing/decreasing case immediately 
# just check first and last element and compare to middle element 

# from there we can comfortably assume nums has a drop somewhere
# left is less and right is more 
