class Solution
{
public:
    vector<int> findCoins(vector<int> &numWays)
    {
        int n = numWays.size();
        vector<long long> dp(n + 1, 0);
        dp[0] = 1; // Base case: one way to make 0
        vector<int> coins;

        for (int i = 1; i <= n; ++i)
        {
            // If current number of ways is less than expected,
            // a new denomination of value 'i' is required.
            if (dp[i] < numWays[i - 1])
            {
                coins.push_back(i);

                // Update dp for all larger amounts using this new coin.
                for (int j = i; j <= n; ++j)
                {
                    dp[j] += dp[j - i];
                    if (dp[j] > 2e8)
                        dp[j] = 2e8 + 1; // Prevent overflow
                }
            }
            // If dp[i] exceeds expected value, configuration is invalid.
            else if (dp[i] > numWays[i - 1])
            {
                return {};
            }
        }

        // Final validation: ensure dp matches numWays exactly.
        for (int i = 1; i <= n; ++i)
        {
            if (dp[i] != numWays[i - 1])
                return {};
        }

        return coins;
    }
};
