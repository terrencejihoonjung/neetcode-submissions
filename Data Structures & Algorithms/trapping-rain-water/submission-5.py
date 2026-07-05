class Solution:
    def trap(self, height: List[int]) -> int:
        # edge case 
        if len(height) == 1: return 0

        ans = 0
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n

        curr_max = 0
        for i in range(n):
            curr_max = max(curr_max, height[i])
            left_max[i] = curr_max
        
        curr_max = 0
        for i in range(n - 1, -1, -1):
            curr_max = max(curr_max, height[i])
            right_max[i] = curr_max 
        
        for i in range(n):
            min_height = min(left_max[i], right_max[i])
            if height[i] < min_height:
                area = (min_height * 1) - height[i]
                ans += area
        
        return ans