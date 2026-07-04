class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []

        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue

            j = i + 1
            k = len(nums) - 1 
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                
                if sum == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]: j += 1
                elif sum > 0: k -= 1
                else: j += 1
        
        return ans



    # to avoid duplicates, we need to sort nums so that we can add checks to skip dupes 
    # for i, skip if current num is == to previous num 
    # for j and k, run a binary search and exhaust it 
    # after finding a solution, move left pointer until dupes are skipped 
