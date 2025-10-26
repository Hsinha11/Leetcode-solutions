// 2719-count-of-integers.cpp
// LeetCode 2719. Count of Integers
// Approach: Digit DP (memoized). Count numbers <= N whose digit-sum is within [min_sum, max_sum].
// Compute ans = count(num2) - count(num1 - 1) (mod 1e9+7).
// Time Complexity: O(L * S * 10) ~ O(L * S) where L = len(N), S = max_sum
// Space Complexity: O(L * S) for memo table

#include <bits/stdc++.h>
using namespace std;
using int64 = long long;
const int MOD = 1000000007;

struct DigitDP {
    string digits;
    int L;
    int min_sum, max_sum;
    // dp[pos][sum][tight] => use -1 for unknown
    vector<vector<array<int64,2>>> dp;

    DigitDP(const string &N, int mn, int mx): digits(N), L(N.size()), min_sum(mn), max_sum(mx) {
        dp.assign(L + 1, vector<array<int64,2>>(max_sum + 1, { -1, -1 }));
    }

    int64 dfs(int pos, int sum, int tight) {
        if (sum > max_sum) return 0;
        if (pos == L) return (sum >= min_sum && sum <= max_sum) ? 1 : 0;
        if (dp[pos][sum][tight] != -1) return dp[pos][sum][tight];
        int limit = tight ? (digits[pos] - '0') : 9;
        int64 res = 0;
        for (int d = 0; d <= limit; ++d) {
            int nt = (tight && (d == limit)) ? 1 : 0;
            res += dfs(pos + 1, sum + d, nt);
            if (res >= MOD) res -= MOD;
        }
        dp[pos][sum][tight] = res;
        return res;
    }

    int64 count_upto() {
        return dfs(0, 0, 1);
    }
};

string dec_str(const string &s) {
    // subtract 1 from non-empty numeric string s (s > "0")
    string out = s;
    int i = (int)out.size() - 1;
    while (i >= 0) {
        if (out[i] == '0') {
            out[i] = '9';
            --i;
        } else {
            out[i] = char(out[i] - 1);
            break;
        }
    }
    // remove leading zeros
    size_t pos = out.find_first_not_of('0');
    if (pos == string::npos) return "0";
    return out.substr(pos);
}

int64 count_of_integers(const string &num1, const string &num2, int min_sum, int max_sum) {
    DigitDP dp2(num2, min_sum, max_sum);
    int64 a = dp2.count_upto() % MOD;

    int64 b = 0;
    if (num1 != "0") {
        string prev = dec_str(num1);
        DigitDP dp1(prev, min_sum, max_sum);
        b = dp1.count_upto() % MOD;
    }

    int64 ans = (a - b) % MOD;
    if (ans < 0) ans += MOD;
    return ans;
}

/*
Example usage:
#include <iostream>
int main() {
    cout << count_of_integers("1", "12", 1, 8) << "\n"; // 11
    cout << count_of_integers("1", "5", 1, 5) << "\n";  // 5
}
*/
