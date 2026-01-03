class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        rowmax = [-1]*n
        # colmax = [-1]*m
        for i in range(n):
            rowmax[i] = max(grid[i])
        # print(rowmax)
        colmax = [max(col) for col in zip(*grid)]
        ans = 0
        for i in range(n):
            for j in range(m):
                ans+= min(rowmax[i],colmax[j]) - grid[i][j]
        return ans