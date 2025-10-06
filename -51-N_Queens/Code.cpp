class Solution {
public:
    bool isSafe(vector<vector<int>>& board, int row, int col) {
        int x = row, y = col;
        while(y >= 0) {
            if(board[x][y--] == 1)  return false;
        }
        y = col;
        while(x < board.size() && y >= 0) {
            if(board[x++][y--] == 1)    return false;
        }
        x = row, y = col;
        while(x >= 0 && y >= 0) {
            if(board[x--][y--] == 1)    return false;
        }
        return true;
    }

    void addSol(vector<vector<int>>& board, int n, vector<vector<string>>& ans) {
        vector<string>arr;
        for(int i = 0; i < n; i++) {
            string str = "";
            for(int j = 0;  j< n; j++) {
                if(board[i][j] == 1)        str.push_back('Q');
                else    str.push_back('.');
            }
            arr.push_back(str);
        }
        ans.push_back(arr);
    }

    void solve(vector<vector<int>>& board, int n, int col, vector<string>& v, vector<vector<string>>& ans) {
        if(col == n) {
            addSol(board, n, ans);
            return ;
        }
        for(int row = 0; row < n; row++) {
            if(isSafe(board, row, col)) {
                board[row][col] = 1;
                solve(board, n, col + 1, v, ans);
                board[row][col] = 0;
            }
        }
    }

    vector<vector<string>> solveNQueens(int n) {
        vector<vector<int>>board(n, vector<int>(n, 0));
        vector<string>v;
        vector<vector<string>>ans;
        solve(board, n, 0, v, ans);
        return ans;
    }
};
