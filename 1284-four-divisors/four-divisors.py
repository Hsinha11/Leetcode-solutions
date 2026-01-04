class Solution:
    def getDiv(self,n: int) -> list[int]:
        small = []
        large = []
        limit = int(math.isqrt(n))  # exact integer sqrt
        for i in range(1, limit + 1):
            if n % i == 0:
                small.append(i)
                if i != n // i:      # avoid double-counting squares
                    large.append(n // i)
        return small + large[::-1]

    def sumFourDivisors(self, nums: List[int]) -> int:
        s = 0
        for i in nums:
            a = self.getDiv(i)
            if len(a)==4:
                s+=sum(a)
        return s