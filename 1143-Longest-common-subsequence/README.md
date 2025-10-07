# 1143. Longest Common Subsequence

## Problem Link
[LeetCode - 1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)

## Problem Description
Given two strings `text1` and `text2`, return the length of their **longest common subsequence**.  
If there is no common subsequence, return `0`.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example:
- "ace" is a subsequence of "abcde".
- "aec" is **not** a subsequence of "abcde".

A **common subsequence** of two strings is a subsequence that appears in both.

### Example 1
**Input:**  
`text1 = "abcde", text2 = "ace"`  
**Output:**  
`3`  
**Explanation:**  
The longest common subsequence is `"ace"` and its length is `3`.

### Example 2
**Input:**  
`text1 = "abc", text2 = "abc"`  
**Output:**  
`3`  
**Explanation:**  
The longest common subsequence is `"abc"` and its length is `3`.

### Example 3
**Input:**  
`text1 = "abc", text2 = "def"`  
**Output:**  
`0`  
**Explanation:**  
There is no such common subsequence, so the result is `0`.

### Constraints
- `1 <= text1.length, text2.length <= 1000`
- `text1` and `text2` consist of only lowercase English characters.

---

## Approach
We use **Dynamic Programming (DP)** to solve this problem efficiently.

Let `dp[i][j]` represent the length of the longest common subsequence between the first `i` characters of `text1` and the first `j` characters of `text2`.

### Transition:
- If `text1[i-1] == text2[j-1]`  
  → `dp[i][j] = 1 + dp[i-1][j-1]`
- Else  
  → `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`

The final answer is stored in `dp[n][m]`, where `n` and `m` are the lengths of `text1` and `text2`.

---

## Time Complexity
O(n × m)

## Space Complexity
O(n × m)

