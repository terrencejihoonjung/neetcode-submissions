class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        forward = [1] * n
        for i in range(n - 1):
            forward[i + 1] = nums[i] * forward[i]
        
        backward = [1] * n
        for i in range(n - 1):
            idx = n - i - 1
            backward[idx - 1] = backward[idx] * nums[idx]
        
        ans = [1] * n
        for i in range(n):
            ans[i] = forward[i] * backward[i]
        
        return ans
