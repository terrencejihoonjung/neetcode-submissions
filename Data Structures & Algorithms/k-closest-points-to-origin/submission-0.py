import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for x,y in points:
            distance = self.calculateEuclideanDistanceToOrigin(x, y)
            heapq.heappush(min_heap, (distance, [x, y]))

        return [point[1] for point in heapq.nsmallest(k, min_heap)]
    
    def calculateEuclideanDistanceToOrigin(self, x: int, y: int) -> float:
        num = x**2 + y**2
        print(num)
        return math.sqrt(num)