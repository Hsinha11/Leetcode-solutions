class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = energy
        for i in range(n-k-1,-1,-1):
            dp[i] = dp[i] + dp[i+k]
        # print(dp)
        
        return max(dp)