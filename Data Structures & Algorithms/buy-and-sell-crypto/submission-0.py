class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        min_price = float("inf")
        for price in prices:
            min_price = min(min_price, price)

            current_prof = price - min_price

            max_prof = max(max_prof, current_prof)

        return max_prof

