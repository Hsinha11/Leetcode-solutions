#include <vector>
#include <queue>
#include <tuple>
using namespace std;

class Solution {
public:
    int trapRainWater(vector<vector<int>>& heightMap) {
        if (heightMap.empty() || heightMap[0].empty()) return 0;
        int m = heightMap.size(), n = heightMap[0].size();
        if (m < 3 || n < 3) return 0;

        typedef tuple<int,int,int> T;
        priority_queue<T, vector<T>, greater<T>> pq;
        vector<vector<bool>> visited(m, vector<bool>(n, false));

        // Push all boundary cells into min-heap
        for (int i = 0; i < m; ++i) {
            pq.emplace(heightMap[i][0], i, 0); visited[i][0] = true;
            pq.emplace(heightMap[i][n-1], i, n-1); visited[i][n-1] = true;
        }
        for (int j = 0; j < n; ++j) {
            if (!visited[0][j]) { pq.emplace(heightMap[0][j], 0, j); visited[0][j] = true; }
            if (!visited[m-1][j]) { pq.emplace(heightMap[m-1][j], m-1, j); visited[m-1][j] = true; }
        }

        int res = 0;
        int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};

        while (!pq.empty()) {
            T cell = pq.top(); pq.pop();
            int h = get<0>(cell);
            int r = get<1>(cell);
            int c = get<2>(cell);

            for (int k = 0; k < 4; ++k) {
                int nr = r + dirs[k][0];
                int nc = c + dirs[k][1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || visited[nr][nc]) continue;
                visited[nr][nc] = true;
                int nh = heightMap[nr][nc];
                if (nh < h) res += h - nh;
                pq.emplace(max(nh, h), nr, nc);
            }
        }
        return res;
    }
};
