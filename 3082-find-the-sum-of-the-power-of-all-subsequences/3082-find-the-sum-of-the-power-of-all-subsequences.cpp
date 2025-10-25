#include <vector>
using namespace std;

// Approach: Use DP to count subsequences summing to k for all subsequences.
// Time: O(n*k), Space: O(k)
class Solution {
public:
    int sumOfPower(vector<int>& nums, int k) {
        const int MOD = 1e9 + 7;
        vector<int> dp(k + 1, 0);
        dp[0] = 1; // empty subsequence

        for (int num : nums) {
            for (int s = k; s >= num; --s) {
                dp[s] = (dp[s] + dp[s - num]) % MOD;
            }
        }
        return dp[k] % MOD;
    }
};
