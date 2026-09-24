class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.nums = nums
    
        def backtrack(i: int, arr: List[int]) -> None:
            if i == len(self.nums): 
                self.res.append(arr[:])
                return 

            arr.append(self.nums[i])
            backtrack(i + 1, arr)
            arr.pop()
            backtrack(i + 1, arr)

        
        backtrack(0, [])
        return self.res



# what is defined as a subset
# - any combination of ordered values, including empty set

# iterate through nums 
# - treat each num as the "base" of a subset you are building
# - for that subset being built, iterate through the rest of the elements 

# backtrack, early return when previously built subset's length is equal to nums 
# - should take in nums, current index, and subset being built 