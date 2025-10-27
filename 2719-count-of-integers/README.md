### 2719-count-of-integers

**Approach:** Digit DP — count numbers <= N with digit sum in [min_sum, max_sum] using memoized DFS over positions, tight flag, and current sum. Answer = count(num2) - count(num1 - 1) (mod 1e9+7).

**Complexity:** Time O(L * S) where L = length of N and S = max_sum, Space O(L * S)
