class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        max_area = 0
        while left < right:
            # calculate max area
            area = (right - left) * min(heights[left], heights[right])
            max_area = max(max_area, area)

            # update left or right pointer
            if heights[left] < heights[right]:
                left += 1
            else: right -= 1
        
        return max_area
