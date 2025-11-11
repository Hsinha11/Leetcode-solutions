class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        tuples= [None]*len(strs)
        for i in range(len(strs)):
            z = strs[i].count('0')
            o = strs[i].count('1')
            tuples[i] = (z,o)
        dp = [[[0] * (m + 1) for _ in range(n + 1)] for _ in range(len(tuples) + 1)]

        # Process each tuple one by one
        for i in range(1, len(tuples) + 1):
            a, b = tuples[i - 1]
            for j in range(n + 1):
                for k in range(m + 1):
                    # Not picking the current tuple
                    dp[i][j][k] = dp[i - 1][j][k]
                    
                    # Picking the current tuple if it fits within the constraints
                    if j >= b and k >= a:
                        dp[i][j][k] = max(dp[i][j][k], 1 + dp[i - 1][j - b][k - a])

        # The maximum subset length with sum constraints
        return dp[len(tuples)][n][m]

