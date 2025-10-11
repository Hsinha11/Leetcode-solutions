# Letter Combinations of a Phone Number

## Problem Statement

Given a string containing digits from `2` to `9`, return all possible letter combinations that the number could represent.  
The mapping of digits to letters (like on a telephone keypad) is as follows:

| Digit | Letters  |
|:------:|:---------|
| 2 | a, b, c |
| 3 | d, e, f |
| 4 | g, h, i |
| 5 | j, k, l |
| 6 | m, n, o |
| 7 | p, q, r, s |
| 8 | t, u, v |
| 9 | w, x, y, z |

Return the combinations **in any order**.  
If the input string is empty, return an empty list.

**Example:**
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

## Approach Explanation

This solution uses **backtracking** — a recursive technique to build all possible combinations step-by-step.

### Steps:
1. Create a mapping (`keypad`) of digits to corresponding letters.
2. Start from the first digit and try all letters mapped to it.
3. For each letter, recursively build combinations for the next digit.
4. Once all digits are used, add the formed string to the result list.
5. Use backtracking (removing last character) to explore new combinations.

### Key Idea:
At each step, we **branch** for each possible letter mapped to the current digit, forming a **recursion tree**.

---

## Time and Space Complexity

| Complexity | Analysis |
|:------------|:----------|
| **Time** | O(3ⁿ × 4ᵐ) — where n is the count of digits mapping to 3 letters and m is count mapping to 4 letters (7,9). Each recursive path builds one combination. |
| **Space** | O(k) for recursion depth + O(N) for output list, where k = number of digits, N = total combinations. |

---

## Example Walkthrough

**Input:** `digits = "23"`

**Step-by-step:**
- Digit '2' → [a, b, c]
- Digit '3' → [d, e, f]

- Start with '2':
- a → combine with [d, e, f] → ad, ae, af
- b → combine with [d, e, f] → bd, be, bf
- c → combine with [d, e, f] → cd, ce, cf

**Result:**
- ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

---

## Summary

| Aspect | Description |
|:-------|:-------------|
| **Algorithm Type** | Backtracking |
| **Data Structure Used** | StringBuilder, Recursion |
| **Edge Cases** | Empty string input |
| **Language** | Java |

---


Contributed for **Hacktoberfest 2025**  
By *Shreeja Hebbar* 