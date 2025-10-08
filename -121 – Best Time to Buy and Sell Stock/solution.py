from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = prices[0]   # Minimum price seen so far
        max_profit = 0          # Maximum profit so far

        for price in prices:
            # Update the minimum price if current price is lower
            if price < min_price:
                min_price = price
            # Calculate profit if selling today, update max profit if better
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
