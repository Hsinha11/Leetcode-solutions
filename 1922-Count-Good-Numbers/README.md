# Count Good Numbers

This project implements a solution to the **Count Good Numbers** problem. The goal is to calculate the number of "good" numbers of length `n` under specific constraints, using efficient modular exponentiation.

---

## Problem Description

A number is considered **good** if:

- Digits at **even positions** (0-indexed) are **even digits**: 0, 2, 4, 6, 8  
- Digits at **odd positions** (0-indexed) are **prime digits**: 2, 3, 5, 7  

Given an integer `n`, count the total number of good numbers of length `n`. Since the result can be very large, return it **modulo** 10^9 + 7.

---

## Solution Approach

The solution uses **fast modular exponentiation**:

1. Count the number of digits in **even positions**: `even = ceil(n / 2)`  
2. Count the number of digits in **odd positions**: `odd = n // 2`  
3. Compute `5^even * 4^odd % (10^9 + 7)` using recursive exponentiation.

The recursion ensures that the computation is efficient even for large values of `n`.

---

## Code Example

```python
from math import ceil

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        def power(x, n):
            if n == 0:
                return 1
            if n < 0:
                return 1 / power(x, -n)
            half = power(x, n // 2) % MOD
            if n % 2 == 0:
                return (half * half) % MOD
            else:
                return (half * half * x) % MOD

        even = ceil(n / 2)
        odd = n // 2
        return (power(5, even) * power(4, odd)) % MOD

# Example usage
solution = Solution()
print(solution.countGoodNumbers(3))  # Output: 100


Time Complexity

Exponentiation: O(log n)

Overall complexity: O(log n)

Space Complexity

Recursive calls stack: O(log n)

Otherwise, O(1)