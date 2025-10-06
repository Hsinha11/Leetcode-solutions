import java.util.*;

class Solution {
    public boolean isSafe(int[][] board, int row, int col) {
        int x = row, y = col;

        // Check left side of the current row
        while (y >= 0) {
            if (board[x][y--] == 1)
                return false;
        }

        // Check upper diagonal on left side
        y = col;
        while (x < board.length && y >= 0) {
            if (board[x++][y--] == 1)
                return false;
        }

        // Check lower diagonal on left side
        x = row;
        y = col;
        while (x >= 0 && y >= 0) {
            if (board[x--][y--] == 1)
                return false;
        }

        return true;
    }

    public void addSol(int[][] board, int n, List<List<String>> ans) {
        List<String> arr = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            StringBuilder str = new StringBuilder();
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 1)
                    str.append('Q');
                else
                    str.append('.');
            }
            arr.add(str.toString());
        }
        ans.add(arr);
    }

    public void solve(int[][] board, int n, int col, List<String> v, List<List<String>> ans) {
        if (col == n) {
            addSol(board, n, ans);
            return;
        }

        for (int row = 0; row < n; row++) {
            if (isSafe(board, row, col)) {
                board[row][col] = 1;
                solve(board, n, col + 1, v, ans);
                board[row][col] = 0;
            }
        }
    }

    public List<List<String>> solveNQueens(int n) {
        int[][] board = new int[n][n];
        List<String> v = new ArrayList<>();
        List<List<String>> ans = new ArrayList<>();
        solve(board, n, 0, v, ans);
        return ans;
    }
}
