import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [stone for stone in stones]
        heapq.heapify_max(max_heap)

        while len(max_heap) > 1:
            s1 = heapq.heappop_max(max_heap)
            s2 = heapq.heappop_max(max_heap)

            if s1 != s2: 
                new_weight = abs(s2 - s1)
                heapq.heappush_max(max_heap, new_weight)
        
        return max_heap[0] if len(max_heap) == 1 else 0