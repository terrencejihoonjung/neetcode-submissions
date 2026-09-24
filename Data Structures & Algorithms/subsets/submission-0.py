class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = [[]]
    
        def backtrack(nums: List[int], i: int, arr: List[int]) -> None:
            if i == len(nums): return 

            for idx in range(i, len(nums)): 
                arr.append(nums[idx])
                self.res.append(arr.copy())
                backtrack(nums, idx + 1, arr)
                arr.pop()

        
        backtrack(nums, 0, [])
        return self.res



# what is defined as a subset
# - any combination of ordered values, including empty set

# iterate through nums 
# - treat each num as the "base" of a subset you are building
# - for that subset being built, iterate through the rest of the elements 

# backtrack, early return when previously built subset's length is equal to nums 
# - should take in nums, current index, and subset being built 