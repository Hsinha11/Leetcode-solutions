#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> triangle;
        triangle.reserve(numRows);
        for (int r = 0; r < numRows; ++r) {
            vector<int> row(r + 1, 1);
            for (int c = 1; c < r; ++c) {
                row[c] = triangle[r - 1][c - 1] + triangle[r - 1][c];
            }
            triangle.push_back(move(row));
        }
        return triangle;
    }
};

// Helper main for quick local testing
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    Solution sol;
    auto res = sol.generate(n);
    for (const auto& row : res) {
        for (int i = 0; i < (int)row.size(); ++i) {
            if (i) cout << ' ';
            cout << row[i];
        }
        cout << "\n";
    }
    return 0;
}


