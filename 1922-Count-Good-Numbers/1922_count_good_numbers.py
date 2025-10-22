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

# Test cases
solution = Solution()

test_cases = [
    1,   # Smallest possible n
    2,   # Small even n
    3,   # Small odd n
    4,   # Even n
    10,  # Larger n
    50,  # Much larger n
]

for n in test_cases:
    print(f"countGoodNumbers({n}) = {solution.countGoodNumbers(n)}")
