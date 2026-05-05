class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        
        def feasible(c):
            req_days = 1
            cur_w = 0
            for w in weights:
                if cur_w + w <= c:
                    cur_w += w
                else:
                    req_days += 1
                    cur_w = w
            if req_days > days:
                return False
            else:
                return True
        
        low = max(weights)
        high = sum(weights)

        while low < high:
            mid = low + (high - low) // 2
            if feasible(mid):
                high = mid
            else:
                low = mid + 1
        return low