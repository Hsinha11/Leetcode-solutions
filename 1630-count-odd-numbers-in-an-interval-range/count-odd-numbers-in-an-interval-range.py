class Solution:
    def countOdds(self, low: int, high: int) -> int:
        N  = (high - low +1)
        if N%2==0:
            return N//2
        else:
            if low%2!=0 and high%2!=0:
                return N//2+1
            else:
                return N//2