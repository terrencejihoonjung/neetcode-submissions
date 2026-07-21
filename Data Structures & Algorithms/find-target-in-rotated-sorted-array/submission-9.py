class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1: return 0 if nums[0] == target else -1

        left = 0
        right = len(nums) - 1

        while left <= right: 
            mid = (left + right) // 2
            if nums[mid] == target: return mid

            if nums[mid] > nums[right]:
                if target <= nums[mid] and target >= nums[left]:
                    right = mid - 1
                else: 
                    left = mid + 1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else: 
                    left = mid + 1

        return -1
# seems similar to find min in rotated sorted array problem
# maybe only thing to change is the how we compare mid with left and right 

# this involves 2 layers of checks: 1) locate where mid is and 2) locate where target is 
# this involves 4 cases 

# (1) mid is on left section and target is in left section 
#   - mid >= left and mid <= target and target > right -> right = mid 
# (2) mid is on left section and target is in right section
#   - mid >= left and mid <= target and target <= right -> left = mid + 1
# (3) mid is on right section and target is in left section
#   - 
# (4) mid is on right section and target is in right section