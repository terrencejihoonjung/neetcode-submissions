class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        initial = self.isMonotonic(nums)
        if initial[0]: return initial[1]

        # use binary search on nums to find the drop/min element in the middle
        left = 0 
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2

            result = self.isMonotonic(nums[left:right + 1])
            if result[0]: return result[1]

            elif nums[left] <= nums[mid] and nums[right] <= nums[mid]:
                left = mid + 1

            elif nums[left] >= nums[mid] and nums[right] >= nums[mid]:
                right = mid
            
        return nums[right]

    def isMonotonic(self, nums) -> (bool, int):
        # check monotonically increasing/decreasing case
        first = nums[0]
        last = nums[-1]
        mid = nums[(len(nums)-1) // 2]

        if first < mid < last: return (True, first)
        if first > mid > last: return (True, last)

        return (False, -1)



# we can eliminate monotonically increasing/decreasing case immediately 
# just check first and last element and compare to middle element 

# from there we can comfortably assume nums has a drop somewhere
# left is less and right is more 
