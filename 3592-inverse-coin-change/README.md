# LeetCode 3592: Inverse Coin Change

**Problem Link:** [LeetCode - Inverse Coin Change](https://leetcode.com/problems/inverse-coin-change/description/)

---

## Problem Statement

You are given an array `coins` of distinct positive integers representing coin denominations, and an integer `amount`.

You need to find the minimum number of coins required to make up that amount in reverse — that is, given a list of coin counts, you must determine the possible denominations that could produce them.  

Formally, the task is to determine if there exists a set of coin denominations that could lead to a given sequence of minimum coin counts for each prefix amount from `1` to `amount`.  
If such a set exists, return any valid set of denominations.  
If not, return an empty array.

---

## Approach Explanation

1. **Understanding the "Inverse" Nature**  
   Normally, in the classic Coin Change problem, we know the coin denominations and try to find the minimum number of coins required for each amount.  
   In this "inverse" version, we are given the results (minimum coin counts for each prefix amount) and need to infer the coin denominations.

2. **Key Insight**  
   - If `dp[i]` denotes the minimum number of coins needed to form amount `i`,  
     then adding a coin of denomination `d` affects all `dp[i + d]`.
   - The difference `dp[i + 1] - dp[i]` gives insight into whether a new denomination must exist.

3. **Algorithm Steps**
   - Iterate through the array of `dp` values (given as input).
   - Whenever `dp[i]` increases by 1 compared to `dp[i - 1]`, that implies the presence of a coin of value `i`.
   - Use this pattern to extract potential coin denominations.

4. **Validation**
   - Once the candidate denominations are found, re-simulate the coin change process.
   - If the recomputed `dp` array matches the given one, return the denominations.
   - Otherwise, return an empty array.

---

## Time and Space Complexity

| Complexity Type | Analysis |
|-----------------|-----------|
| **Time Complexity** | `O(n * k)` — where `n` is the amount and `k` is the number of inferred denominations, since we may need to simulate the DP verification. |
| **Space Complexity** | `O(n)` — we use an auxiliary DP array to verify the correctness of inferred denominations. |

---

## Example Walkthrough

### Example
**Input:**  
`coinsNeeded = [1,1,2,2,3,3,3,4]`

**Explanation Step-by-Step:**

1. The sequence shows when a new coin denomination might appear:
   - `dp[1] = 1` → new denomination (1)
   - `dp[3] = 2` → new denomination (2)
   - `dp[7] = 3` → new denomination (4)

   Thus, inferred denominations: `[1, 2, 4]`

2. **Validation using Classic Coin Change:**
   - Using coins `[1, 2, 4]`, simulate the standard DP.
   - The computed minimum coins for amounts 1 through 8 match `[1,1,2,2,3,3,3,4]`.

Therefore, the output is `[1, 2, 4]`.

---

## Final Answer

**Output:**  
`[1, 2, 4]`

---

## Summary

| Section | Key Point |
|----------|------------|
| **Goal** | Reverse-engineer coin denominations from a list of minimum coin counts. |
| **Core Idea** | A new denomination appears when the coin count increases by 1 after a plateau. |
| **Verification** | Simulate coin change DP using inferred denominations. |
| **Edge Cases** | Non-monotonic or invalid sequences should return an empty array. |

---
