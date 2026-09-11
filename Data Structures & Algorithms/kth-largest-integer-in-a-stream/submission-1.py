import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = nums
        self.k = k
        heapq.heapify(self.min_heap)

        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        
        return self.min_heap[0]
        
# initialize and build max-heap using nums -> O(m)
# during add, we add to the heap and find kth largest integer -> O(m + logk)