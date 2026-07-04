class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1: return [0]

        ans = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while len(stack) > 0 and stack[-1][1] < temperatures[i]:
                popped = stack.pop()
                ans[popped[0]] = i - popped[0]
            stack.append([i, temperatures[i]])
        
        return ans
    
    # iterate through temperatures and add to the stack [index, temp]
    # while the top of a stack's temp is less than the current temp, 
        # assign that top stack's index, currIdx - topIdx