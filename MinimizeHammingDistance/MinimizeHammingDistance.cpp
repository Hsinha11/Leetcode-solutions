#include <bits/stdc++.h>
using namespace std;

// ============================
// Disjoint Set Union (Union-Find)
// ============================
class DSU {
public:
    vector<int> parent, rank;
    DSU(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        for (int i = 0; i < n; i++) parent[i] = i;
    }
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    void unite(int x, int y) {
        int rx = find(x), ry = find(y);
        if (rx == ry) return;
        if (rank[rx] < rank[ry]) parent[rx] = ry;
        else if (rank[ry] < rank[rx]) parent[ry] = rx;
        else parent[ry] = rx, rank[rx]++;
    }
};

// ============================
// Solution Class
// ============================
class Solution {
public:
    int minimumHammingDistance(vector<int>& source, vector<int>& target, vector<vector<int>>& allowedSwaps) {
        int n = source.size();
        DSU dsu(n);

        // Step 1: Union all allowed swaps
        for (auto &p : allowedSwaps) {
            dsu.unite(p[0], p[1]);
        }

        // Step 2: Group indices by connected components (root)
        unordered_map<int, vector<int>> components;
        for (int i = 0; i < n; i++) {
            components[dsu.find(i)].push_back(i);
        }

        // Step 3: Calculate mismatches in each component
        int hammingDistance = 0;
        for (auto &compEntry : components) {
            auto &indices = compEntry.second;
            unordered_map<int, int> freqSource, freqTarget;

            for (int idx : indices) {
                freqSource[source[idx]]++;
                freqTarget[target[idx]]++;
            }

            for (auto &entry : freqSource) {
                int value = entry.first;
                int countInSource = entry.second;
                int countInTarget = freqTarget[value];

                // Elements that cannot be matched contribute to mismatch
                hammingDistance += max(0, countInSource - countInTarget);
            }
        }

        return hammingDistance;
    }
};

// ============================
// Main Function (Example Test)
// ============================
int main() {
    vector<int> source = {5,1,2,4,3};
    vector<int> target = {1,5,4,2,3};
    vector<vector<int>> allowedSwaps = {{0,4},{4,2},{1,3},{1,4}};

    Solution sol;
    cout << "Minimum Hamming Distance: " << sol.minimumHammingDistance(source, target, allowedSwaps) << endl;

    return 0;
}
