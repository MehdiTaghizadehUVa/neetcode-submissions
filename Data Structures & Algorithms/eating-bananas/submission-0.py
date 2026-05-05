class Solution:
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(k):
            required_hour = 0
            for pile in piles:
                required_hour += (pile + k - 1) // k
            
            if required_hour > h:
                return False
            else:
                return True
        low = 1
        high = max(piles)
        mid = low + ((high - low) // 2)

        while low < high:
            if feasible(mid):
                high = mid
            else:
                low = mid + 1
            
            mid = low + ((high - low) // 2)
        
        return low