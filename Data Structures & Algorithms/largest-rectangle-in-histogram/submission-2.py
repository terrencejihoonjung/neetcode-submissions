class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        global_area = 0
        stack = []

        for i, height in enumerate(heights):
            start = i

            while len(stack) > 0 and height < stack[-1][1]:
                popped = stack.pop()
                global_area = max(global_area, popped[1] * (i - popped[0]))
                start = popped[0]

            stack.append((start, height))
        
        for item in stack:
            global_area = max(global_area, (len(heights) - item[0]) * item[1])
        
        return global_area


        # for i, height in heights
        #   start = i
        #   while curr_height < top_of_stack_height: 
        #       pop from stack
        #       calculate area and update global area
        #       start = top_of_stack_idx
        #    
        #   append (start, height) to stack

        # for item in stack
        #   calculate and update max area (width = len(heights) - i)