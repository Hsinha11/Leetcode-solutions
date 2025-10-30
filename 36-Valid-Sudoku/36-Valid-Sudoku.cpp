#include <bits/stdc++.h>
using namespace std;

class Solution{
public:
    bool isValidSudoku(vector<vector<char>>& board){
        vector<vector<int>> rows(9, vector<int>(9, 0));
        vector<vector<int>> cols(9, vector<int>(9, 0));
        vector<vector<int>> boxes(9, vector<int>(9, 0));

        for(int i = 0; i < 9; i++){
            for(int j = 0; j < 9; j++){
                if(board[i][j] == '.') continue;

                int num = board[i][j] - '1';
                int boxIndex = (i/3)*3 + (j/3);

                if(rows[i][num] || cols[j][num] || boxes[boxIndex][num])
                    return false;

                rows[i][num] = cols[j][num] = boxes[boxIndex][num] = 1;
            }
        }
        return true;
    }
};