### Code (Python)

from bisect import bisect_right
from typing import List

class Solution:
  def mincostTickets(self, days: List[int], costs: List[int]) -> int:
      """
      Return the minimum cost to cover all travel days in `days`.
      """
      n = len(days)
      memo = {}

      def dp(i: int) -> int:
          """
          Returns the minimum cost to cover travel from days[i] to end.
          """
          # Base case: no more days to cover
          if i >= n:
              return 0

          if i in memo:
              return memo[i]

          # Option 1: buy 1-day ticket for days[i]
          cost1 = costs[0] + dp(i + 1)

          # Option 2: buy 7-day ticket starting at days[i]
          # Find first day index > days[i] + 7 - 1
          j = bisect_right(days, days[i] + 7 - 1)
          cost7 = costs[1] + dp(j)

          # Option 3: buy 30-day ticket starting at days[i]
          k = bisect_right(days, days[i] + 30 - 1)
          cost30 = costs[2] + dp(k)

          res = min(cost1, cost7, cost30)
          memo[i] = res
          return res

      return dp(0)