class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right: 
            mid = (left + right) // 2
            
            if self.isRateValid(piles, h, mid):
                right = mid 
            else:
                left = mid + 1
        
        return right

        
    def isRateValid(self, piles, h, k) -> bool:
        duration = 0

        for pile in piles: 
            time = math.ceil(pile / k)
            duration += int(time)
        
        return duration <= h