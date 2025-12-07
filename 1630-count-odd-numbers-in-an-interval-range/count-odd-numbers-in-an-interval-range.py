class Solution:
    def countOdds(self, low: int, high: int) -> int:
        N  = (high - low +1)
        half = N//2
        if N%2==0:
            return half
        else:
            if low%2!=0 and high%2!=0:
                return half+1
            else:
                return half