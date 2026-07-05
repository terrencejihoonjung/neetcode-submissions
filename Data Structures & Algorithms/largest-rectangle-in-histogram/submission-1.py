class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        global_area = 0
        n = len(heights)

        for i in range(n):
            min_height = heights[i]
            left = i
            right = i

            while left - 1 >= 0 and heights[left - 1] >= min_height: 
                min_height = min(min_height, heights[left - 1])
                left -= 1
            while right + 1 < n and heights[right + 1] >= min_height: 
                min_height = min(min_height, heights[right + 1])
                right += 1

            width = right - left + 1
            global_area = max(global_area, width * min_height)
        
        return global_area



    # for each height:
    #   iterate left and right until the next is less than the current bar's height 
    #   calculate the max area for this iteration = min(range's heights) * (right - left + 1)
    #   update global_max