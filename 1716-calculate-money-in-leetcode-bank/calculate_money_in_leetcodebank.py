class Solution:
    def totalMoney(self, n: int) -> int:
        weeks, days = divmod(n, 7)
        total = weeks * 28 + 7 * (weeks * (weeks - 1)) // 2
        
        start = weeks + 1  
        for i in range(days):
            total += start + i
        
        return total