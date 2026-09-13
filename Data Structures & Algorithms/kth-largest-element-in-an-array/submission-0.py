import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k == 1: return max(nums)

        max_heap = nums
        heapq.heapify_max(max_heap)

        return heapq.nlargest(k, max_heap)[-1]