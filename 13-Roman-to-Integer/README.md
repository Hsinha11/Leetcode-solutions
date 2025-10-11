# LeetCode 13: Roman to Integer

**Problem Link:** [LeetCode - Roman to Integer](https://leetcode.com/problems/roman-to-integer/description/)

---

## 🧩 Problem Statement

Roman numerals are represented by seven different symbols:

| Symbol | Value |
|:-------|:------|
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

Given a Roman numeral string `s`, convert it into an integer.

Roman numerals are usually written largest to smallest from left to right.  
However, if a smaller numeral appears **before** a larger one, it means **subtraction**.

**Examples:**
- `IV = 4` (5 - 1)
- `IX = 9` (10 - 1)
- `XL = 40` (50 - 10)
- `XC = 90` (100 - 10)
- `CD = 400` (500 - 100)
- `CM = 900` (1000 - 100)

---

## 💡 Approach Explanation

1. **Mapping Roman Symbols to Integers**  
   Use a hash map to store the value of each Roman symbol.

2. **Subtraction Rule Insight**  
   - If a smaller value precedes a larger one, subtract it.  
   - Otherwise, add it to the running total.

3. **Algorithm Steps**
   - Initialize a total sum as `0`.
   - Traverse the string from left to right.
   - For each character `s[i]`:
     - If `s[i]` < `s[i+1]`, subtract its value.
     - Else, add its value.
   - Return the total.

---

## ⏱️ Time and Space Complexity

| Complexity | Analysis |
|-------------|-----------|
| **Time Complexity** | `O(n)` — each character is processed once |
| **Space Complexity** | `O(1)` — constant map of 7 symbols |

---

## 🧠 Example Walkthrough

**Example:**  
`s = "MCMXCIV"`

| Symbol | Value | Next | Action | Running Total |
|:-------|:-------|:------|:--------|:---------------|
| M | 1000 | C | Add | 1000 |
| C | 100 | M | Subtract | 900 |
| M | 1000 | X | Add | 1900 |
| X | 10 | C | Subtract | 1890 |
| C | 100 | I | Add | 1990 |
| I | 1 | V | Subtract | 1989 |
| V | 5 | — | Add | **1994** |

✅ **Output:** `1994`

---

## 📘 Summary

| Section | Key Point |
|----------|------------|
| **Goal** | Convert a Roman numeral string into its integer equivalent |
| **Core Logic** | Add or subtract based on comparison with the next symbol |
| **Validation** | Works for all valid Roman numeral combinations |
| **Edge Cases** | Handles subtractive pairs like `IV`, `IX`, `XL`, etc. |

---