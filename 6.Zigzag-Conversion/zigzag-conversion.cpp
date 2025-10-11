#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1 || (int)s.size() <= numRows) return s;
        vector<string> rows(min(numRows, (int)s.size()));
        int curRow = 0;
        int dir = 1; // 1 for down, -1 for up
        for (char c : s) {
            rows[curRow].push_back(c);
            if (curRow == 0) dir = 1;
            else if (curRow == numRows - 1) dir = -1;
            curRow += dir;
        }
        string res;
        for (auto &row : rows) res += row;
        return res;
    }
};

// Helper main for quick local testing
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    int rows;
    if (!(cin >> s >> rows)) return 0;
    Solution sol;
    cout << sol.convert(s, rows) << "\n";
    return 0;
}


