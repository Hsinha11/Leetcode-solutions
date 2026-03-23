class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        mx = [[0]*m for _ in range(n)]
        mx[0][0] = grid[0][0]
        mn = [[0]*m for _ in range(n)]
        mn[0][0] = grid[0][0]
        for i in range(1,m):
            mn[0][i] = mn[0][i-1]*grid[0][i]
            mx[0][i] = mx[0][i-1]*grid[0][i]
        for i in range(1,n):
            mn[i][0] = mn[i-1][0]*grid[i][0]
            mx[i][0] = mx[i-1][0]*grid[i][0]
        for i in range(1,n):
            for j in range(1,m):
                if grid[i][j]<0:# minimum product * negative number = new maximum product
                    mx[i][j] = min(mn[i][j-1],mn[i-1][j])*grid[i][j]
                    mn[i][j] = max(mx[i][j-1],mx[i-1][j])*grid[i][j]
                else: # maximum product * positive number = new maximum product
                    mn[i][j] = min(mn[i][j-1],mn[i-1][j])*grid[i][j]
                    mx[i][j] = max(mx[i][j-1],mx[i-1][j])*grid[i][j]
        if mx[n-1][m-1]<0:
            return -1
        else:
            return mx[n-1][m-1]% (10**9+7)

