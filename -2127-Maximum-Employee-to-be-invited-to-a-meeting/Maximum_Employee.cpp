#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maximumInvitations(vector<int>& favorite) {
        int n = static_cast<int>(favorite.size());

        vector<int> indegree(n, 0);
        for (int v : favorite) {
            indegree[v]++;
        }

        // depth[i] = longest chain length that ends at i (before entering cycles)
        vector<int> depth(n, 0);
        queue<int> q;
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }

        // Topologically remove nodes not in cycles and compute longest incoming chains
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            int v = favorite[u];
            depth[v] = max(depth[v], depth[u] + 1);
            if (--indegree[v] == 0) {
                q.push(v);
            }
        }

        // Now, nodes with indegree > 0 are part of cycles
        int maxCycle = 0;
        int sumPairs = 0; // sum of lengths for all mutual pairs with their chains

        vector<int> visited(n, 0);
        for (int i = 0; i < n; i++) {
            if (indegree[i] > 0 && !visited[i]) {
                // Explore this cycle
                int cur = i;
                int len = 0;
                while (!visited[cur]) {
                    visited[cur] = 1;
                    cur = favorite[cur];
                    len++;
                }

                if (len == 2) {
                    // Mutual pair a <-> b: add both chains plus 2
                    int a = i;
                    int b = favorite[a];
                    // Ensure we only count each mutual pair once
                    // Mark the two nodes explicitly and use their depths
                    sumPairs += 2 + depth[a] + depth[b];
                } else {
                    maxCycle = max(maxCycle, len);
                }
            }
        }

        return max(maxCycle, sumPairs);
    }
};

// Helper to run basic local tests (not used on LeetCode submission)
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Example usage:
    // Input format for local test:
    // n followed by n integers for favorite array
    // Example:
    // 5
    // 2 2 1 2 2

    int n;
    if (!(cin >> n)) return 0;
    vector<int> favorite(n);
    for (int i = 0; i < n; i++) cin >> favorite[i];
    Solution sol;
    cout << sol.maximumInvitations(favorite) << "\n";
    return 0;
}


