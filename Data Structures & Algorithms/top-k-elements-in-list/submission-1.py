class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1: return [nums[0]]

        freq = {}
        for num in nums: 
            if num not in freq: freq[num] = 1
            else: freq[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for key in freq.keys():
            buckets[freq[key]].append(key)
        
        limit = k
        ans = []
        for bucket in reversed(buckets):
            if len(bucket) == 0: continue

            for num in bucket:
                ans.append(num)
                k -= 1

                if k == 0: return ans
            
        return []

