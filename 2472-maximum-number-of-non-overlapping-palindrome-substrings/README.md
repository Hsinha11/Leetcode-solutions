### 2472-maximum-number-of-non-overlapping-palindrome-substrings

**Approach:** Precompute palindromic substrings with center expansion, then DP where dp[i] is the best result for s[0..i]; for each i try starts j so s[j..i] is a palindrome of length >= k and update dp.  
**Complexity:** Time O(n^2), Space O(n^2) (palindrome table) — dp uses O(n).
