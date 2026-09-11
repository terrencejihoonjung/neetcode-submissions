import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify_max(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush_max(self.heap, val)
        return heapq.nlargest(self.k, self.heap)[-1]
        
# initialize and build max-heap using nums -> O(m)
# during add, we add to the heap and find kth largest integer -> O(m + logk)