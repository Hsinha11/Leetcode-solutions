#include<bits/stdc++.h>
using namespace std;

// Problem 823: Binary Trees With Factors
// Approach: DP with a map counting trees ending at each number
// Time: O(n^2), Space: O(n)
class Solution {
public:
    int numFactoredBinaryTrees(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        unordered_map<int, long> dp;
        const int MOD = 1e9 + 7;
        for(int num : arr) {
            dp[num] = 1; // single node tree
            for(int x : arr) {
                if(x >= num) break;
                if(num % x == 0 && dp.count(num / x)) {
                    dp[num] += dp[x] * dp[num / x] % MOD;
                    dp[num] %= MOD;
                }
            }
        }
        long ans = 0;
        for(auto& [_, count] : dp) ans = (ans + count) % MOD;
        return ans;
    }
};
