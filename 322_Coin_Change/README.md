
# LeetCode Solutions 📊

![LeetCode](https://img.shields.io/badge/LeetCode-Solutions-brightgreen) ![C++](https://img.shields.io/badge/C++11-blue) ![Java](https://img.shields.io/badge/Java-8-orange)

Welcome to my **LeetCode solutions repository**! Here, you'll find a comprehensive collection of my problem-solving journey across various topics and difficulty levels. Each solution is automatically pushed after completion, showcasing my progress and improving skills.

---

## 🌟 Problem: 322. Coin Change

**Difficulty:** 🟡 Medium
**Topics:** Dynamic Programming, Arrays

---

### 📌 Problem Statement

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the **fewest number of coins** that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return **-1**.

You may assume that you have an infinite number of each kind of coin.

---

### 🧩 Examples

**Example 1:**

```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

**Example 2:**

```
Input: coins = [2], amount = 3
Output: -1
```

**Example 3:**

```
Input: coins = [1], amount = 0
Output: 0
```

---

### ⚙️ Constraints

* `1 <= coins.length <= 12`
* `1 <= coins[i] <= 2^31 - 1`
* `0 <= amount <= 10^4`

---

## 🧠 Approach

We use **Dynamic Programming (Bottom-Up)**:

1. Create a `dp` array of size `amount + 1`, initialized with a large value (infinity).
2. Base case: `dp[0] = 0` (0 coins needed for amount 0).
3. For each coin, update the `dp` array for all reachable amounts.
4. Return `dp[amount]` if it’s not infinity, otherwise return `-1`.

---

## ⏱️ Complexity

* **Time Complexity:** `O(amount * n)` where `n = len(coins)`
* **Space Complexity:** `O(amount)`

---

## 💻 C++ Solution

```cpp
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        const int INF = 1e9;
        vector<int> dp(amount + 1, INF);
        dp[0] = 0;

        for (int coin : coins) {
            for (int i = coin; i <= amount; i++) {
                dp[i] = min(dp[i], dp[i - coin] + 1);
            }
        }
        return dp[amount] == INF ? -1 : dp[amount];
    }
};
```

---

## ☕ Java Solution

```java
class Solution {
    public int coinChange(int[] coins, int amount) {
        int INF = 1000000000;
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, INF);
        dp[0] = 0;

        for (int coin : coins) {
            for (int i = coin; i <= amount; i++) {
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }
        return dp[amount] == INF ? -1 : dp[amount];
    }
}
```

---

## 📁 Folder Structure

```plaintext
/LeetCode-Solutions
  ├── Medium
  │   ├── 322_Coin_Change.cpp
  │   ├── 322_Coin_Change.java
  │   └── README.md
```

---
