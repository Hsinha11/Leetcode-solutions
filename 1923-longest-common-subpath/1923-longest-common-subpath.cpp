// 1923-longest-common-subpath.cpp
// Approach: Binary search on subpath length L. For a fixed L, compute rolling hashes
// (double hashing) for every path and intersect the sets. If intersection non-empty,
// L is achievable.
// Time: O(S * log K) where S = total number of nodes across all paths, K = max path length.
// Space: O(S)

#include <bits/stdc++.h>
using namespace std;

using ull = unsigned long long;
using ll = long long;

class Solution {
public:
    int longestCommonSubpath(int n, vector<vector<int>>& paths) {
        const long long MOD1 = 100000000000019LL; // big values (effectively used via ull combine)
        const long long MOD2 = 100000000000033LL;
        const long long BASE = 100007LL;

        auto check = [&](int L)->bool{
            if (L == 0) return true;
            unordered_set<ull> common;
            bool first = true;

            // precompute BASE^L mod both mods (we'll use ll math with mod)
            long long pow1 = 1, pow2 = 1;
            for (int i = 0; i < L; ++i) {
                pow1 = (__int128)pow1 * BASE % MOD1;
                pow2 = (__int128)pow2 * BASE % MOD2;
            }

            for (auto &path : paths) {
                if ((int)path.size() < L) return false;
                long long h1 = 0, h2 = 0;
                unordered_set<ull> cur;
                for (int i = 0; i < L; ++i) {
                    h1 = ((__int128)h1 * BASE + (path[i] + 1)) % MOD1;
                    h2 = ((__int128)h2 * BASE + (path[i] + 1)) % MOD2;
                }
                ull key = ( (ull)h1 << 32 ) ^ (ull)h2;
                cur.insert(key);

                for (int i = L; i < (int)path.size(); ++i) {
                    long long left = path[i - L] + 1;
                    long long right = path[i] + 1;
                    h1 = ( (__int128)h1 * BASE - (__int128)left * pow1 + right ) % MOD1;
                    h2 = ( (__int128)h2 * BASE - (__int128)left * pow2 + right ) % MOD2;
                    if (h1 < 0) h1 += MOD1;
                    if (h2 < 0) h2 += MOD2;
                    ull k = ( (ull)h1 << 32 ) ^ (ull)h2;
                    cur.insert(k);
                }

                if (first) {
                    common = move(cur);
                    first = false;
                } else {
                    // intersect common with cur
                    unordered_set<ull> next;
                    for (auto &v : cur) {
                        if (common.find(v) != common.end()) next.insert(v);
                    }
                    common.swap(next);
                    if (common.empty()) return false;
                }
            }
            return !common.empty();
        };

        int lo = 0;
        int hi = INT_MAX;
        // hi is the minimal length among paths
        hi = paths[0].size();
        for (auto &p : paths) hi = min(hi, (int)p.size());

        int ans = 0;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (check(mid)) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return ans;
    }
};

// Example main for local testing
int main() {
    Solution sol;
    vector<vector<int>> paths = {{0,1,2,3,4},{2,3,4},{4,0,1,2,3}};
    cout << sol.longestCommonSubpath(5, paths) << endl; // expected 2
    return 0;
}
