class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1

        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if nums[slow] == nums[fast]:
                break
        
        slow = 0
        while nums[slow] != nums[fast]:
            slow = nums[slow]
            fast = nums[fast]
        
        return nums[slow]

