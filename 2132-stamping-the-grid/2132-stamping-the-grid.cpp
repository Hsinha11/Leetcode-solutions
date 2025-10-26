// 2132-stamping-the-grid.cpp
// LeetCode 2132. Stamping the Grid
// Approach: 2D prefix sums to find valid stamp placements (submatrix sum == 0).
// Then use a 2D difference array to mark coverage from all stamps and rebuild
// coverage with prefix sums. Verify every 0 in the grid is covered.
//
// Time Complexity: O(m * n)
// Space Complexity: O(m * n)
// Constraints note (only for cpp): 1 <= m * n <= 2*10^5, stamp dims up to 1e5.

#include <vector>
using namespace std;

class Solution {
public:
    bool possibleToStamp(vector<vector<int>>& grid, int stampHeight, int stampWidth) {
        int m = grid.size();
        int n = grid[0].size();

        // build prefix sum ps with size (m+1) x (n+1)
        vector<vector<int>> ps(m + 1, vector<int>(n + 1, 0));
        for (int i = 0; i < m; ++i) {
            int row_sum = 0;
            for (int j = 0; j < n; ++j) {
                row_sum += grid[i][j];
                ps[i + 1][j + 1] = ps[i][j + 1] + row_sum;
            }
        }

        auto rect_sum = [&](int r1, int c1, int r2, int c2) -> int {
            return ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1];
        };

        // difference array (m+1)x(n+1)
        vector<vector<int>> diff(m + 1, vector<int>(n + 1, 0));

        // mark stamp placements where submatrix is all zeros
        for (int i = 0; i + stampHeight <= m; ++i) {
            for (int j = 0; j + stampWidth <= n; ++j) {
                if (rect_sum(i, j, i + stampHeight - 1, j + stampWidth - 1) == 0) {
                    diff[i][j] += 1;
                    diff[i + stampHeight][j] -= 1;
                    diff[i][j + stampWidth] -= 1;
                    diff[i + stampHeight][j + stampWidth] += 1;
                }
            }
        }

        // accumulate diff row-wise
        for (int i = 0; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                diff[i][j] += diff[i][j - 1];
            }
        }

        // accumulate diff column-wise
        for (int j = 0; j < n; ++j) {
            for (int i = 1; i < m; ++i) {
                diff[i][j] += diff[i - 1][j];
            }
        }

        // verify all zeros are covered
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 0 && diff[i][j] <= 0) return false;
            }
        }
        return true;
    }
};
