class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[[0] * k for _ in range(m)] for _ in range(n)]
        # print(dp)
        dp[0][0][grid[0][0] % k] = 1
        # print(dp)/
        for i in range(n):
            for j in range(m):
                val = grid[i][j]
                for rem in range(k):
                    if  i>0 and dp[i-1][j][rem]>0:
                        new_rem = (rem+val)%k
                        dp[i][j][new_rem]+=dp[i-1][j][rem]%(10**9 + 7)
                for rem in range(k):
                    if  j>0 and dp[i][j-1][rem]>0:
                        new_rem = (rem+val)%k
                        dp[i][j][new_rem]+=dp[i][j-1][rem]%(10**9 + 7)
        return dp[n-1][m-1][0]%(10**9 + 7)