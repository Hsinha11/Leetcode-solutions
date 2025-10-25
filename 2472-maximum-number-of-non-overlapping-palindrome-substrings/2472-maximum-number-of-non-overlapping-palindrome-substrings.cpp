// 2472-maximum-number-of-non-overlapping-palindrome-substrings.cpp
// LeetCode 2472. Maximum Number of Non-overlapping Palindrome Substrings
//
// Approach (short):
//   Precompute all palindromic substrings using center expansion (O(n^2)).
//   Then use DP: dp[i] = maximum number of non-overlapping palindromic substrings
//   that end at or before index i. For each i, try every start j where substring
//   s[j..i] is a palindrome and length >= k, and update dp[i] = max(dp[i], (j>0?dp[j-1]:0) + 1).
//   This yields the optimal (non-overlapping) count.
// Time Complexity: O(n^2) due to palindrome precomputation and DP transitions.
// Space Complexity: O(n^2) for palindrome flags (can be reduced), O(n) for dp.
//
// Notes:
//   - n <= 2000 so O(n^2) is acceptable.
//   - This file defines a Solution class with method maxPalindromes(s, k).
//   - A small main is included for quick local testing.
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxPalindromes(string s, int k) {
        int n = s.size();
        if (n == 0 || k > n) return 0;

        // isPal[i][j] == true if s[i..j] is palindrome
        vector<vector<char>> isPal(n, vector<char>(n, 0));

        // center expansion to mark palindromes
        for (int center = 0; center < n; ++center) {
            // odd length palindromes
            int l = center, r = center;
            while (l >= 0 && r < n && s[l] == s[r]) {
                isPal[l][r] = 1;
                --l; ++r;
            }
            // even length palindromes
            l = center; r = center + 1;
            while (l >= 0 && r < n && s[l] == s[r]) {
                isPal[l][r] = 1;
                --l; ++r;
            }
        }

        // dp[i] = max number of non-overlapping palindromic substrings using s[0..i]
        vector<int> dp(n, 0);

        for (int i = 0; i < n; ++i) {
            // carry forward previous best (no new palindrome ending at i)
            dp[i] = (i > 0) ? dp[i-1] : 0;
            // try all possible start positions j such that length >= k
            // j ranges from 0 .. i-k+1
            for (int j = 0; j + k - 1 <= i; ++j) {
                if (isPal[j][i] && (i - j + 1) >= k) {
                    int prev = (j > 0) ? dp[j-1] : 0;
                    dp[i] = max(dp[i], prev + 1);
                }
            }
        }

        return dp[n-1];
    }
};

#ifdef LOCAL_TEST
int main() {
    Solution sol;
    // Example 1
    string s1 = "abaccdbbd";
    int k1 = 3;
    cout << sol.maxPalindromes(s1, k1) << "  (expected 2)\n";

    // Example 2
    string s2 = "adbcda";
    int k2 = 2;
    cout << sol.maxPalindromes(s2, k2) << "  (expected 0)\n";

    return 0;
}
#endif
