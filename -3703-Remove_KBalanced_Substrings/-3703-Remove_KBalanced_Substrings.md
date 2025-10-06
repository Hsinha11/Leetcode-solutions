# Remove K-Balanced Substrings

## Problem Description

Given a string `s` consisting of `'('` and `')'`, and an integer `k`, a substring is **k-balanced** if it is exactly `k` consecutive `'('` followed by `k` consecutive `')'` (i.e., `'(' * k + ')' * k`). The task is to repeatedly remove all non-overlapping k-balanced substrings from `s` until no such substring exists, and return the final string.

### Examples

**Example 1**

- Input: `s = "(())"`, `k = 1`
- Output: `""`
- Explanation:
    - Step 1: Remove `()` → `()`
    - Step 2: Remove `()` → `""`

**Example 2**

- Input: `s = "(()("`, `k = 1`
- Output: `"(("`
- Explanation:
    - Step 1: Remove `()` → `((`
    - Step 2: No more k-balanced substrings.

**Example 3**

- Input: `s = "((()))()()()"`, `k = 3`
- Output: `"()()()"`
- Explanation:
    - Step 1: Remove `((()))` → `()()()`
    - Step 2: No more k-balanced substrings.

## Approach

1. **Iterative Removal**: 
     - Scan the string for non-overlapping k-balanced substrings.
     - Remove all found substrings in one pass.
     - Repeat until no k-balanced substring remains.

2. **Efficient Search**:
     - Use a sliding window of size `2*k` to check for k-balanced substrings.
     - Mark indices for removal to avoid overlapping removals.

3. **String Reconstruction**:
     - After each pass, reconstruct the string from unmarked indices.

## Time Complexity Analysis

- Each pass scans the string in `O(n)` time, where `n` is the length of the string.
- In the worst case, there can be up to `O(n)` passes (if only one k-balanced substring is removed per pass).
- **Overall Time Complexity:** `O(n^2)` in the worst case.

## Space Complexity Analysis

- Additional space is used for marking indices and reconstructing the string.
- **Space Complexity:** `O(n)`.

## Constraints

- `2 <= s.length <= 10^5`
- `s` consists only of `'('` and `')'`
- `1 <= k <= s.length / 2`
