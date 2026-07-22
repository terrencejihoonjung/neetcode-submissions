class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1: return 0 if nums[0] == target else -1

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: return mid 

            if nums[mid] > nums[right]: 
                if target > nums[right] and target < nums[mid]:
                    right = mid - 1
                else: left = mid + 1
            else:
                if target < nums[mid] or target > nums[right]: right = mid - 1
                else: left = mid + 1
        
        return -1

# we'll need to know where mid and targert is during binary search
# a 2-layered check within each iteration 
# - if mid > right, mid is in left section
#   - if target >= left and target < mid, right = mid - 1
#   - else left = mid + 1
# - else mid is in right section 
#   - if target < mid or target is >= left, right = mid - 1
#   - else left = mid + 1


# edge case 
#   - len(nums) == 1: return 0 if nums[0] == target else -1