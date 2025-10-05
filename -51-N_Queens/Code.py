class Solution:
    def isSafe(self, board, row, col):
        x, y = row, col

        # Check left side of the current row
        while y >= 0:
            if board[x][y] == 1:
                return False
            y -= 1

        # Check upper diagonal on left side
        x, y = row, col
        while x < len(board) and y >= 0:
            if board[x][y] == 1:
                return False
            x += 1
            y -= 1

        # Check lower diagonal on left side
        x, y = row, col
        while x >= 0 and y >= 0:
            if board[x][y] == 1:
                return False
            x -= 1
            y -= 1

        return True

    def addSol(self, board, n, ans):
        arr = []
        for i in range(n):
            row_str = ''.join('Q' if board[i][j] == 1 else '.' for j in range(n))
            arr.append(row_str)
        ans.append(arr)

    def solve(self, board, n, col, v, ans):
        if col == n:
            self.addSol(board, n, ans)
            return

        for row in range(n):
            if self.isSafe(board, row, col):
                board[row][col] = 1
                self.solve(board, n, col + 1, v, ans)
                board[row][col] = 0

    def solveNQueens(self, n):
        board = [[0] * n for _ in range(n)]
        v = []
        ans = []
        self.solve(board, n, 0, v, ans)
        return ans
