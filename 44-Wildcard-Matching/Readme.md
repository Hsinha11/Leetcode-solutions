# Wildcard Matching

## Difficulty: Hard

### Problem Statement

Given an input string `s` and a pattern `p`, implement wildcard pattern matching with support for `?` and `*` where:

- `?` matches any single character.
- `*` matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

### Examples

- **Example 1**:
  - **Input**: `s = "aa"`, `p = "a"`
  - **Output**: `false`
  - **Explanation**: `"a"` does not match the entire string `"aa"`.

- **Example 2**:
  - **Input**: `s = "aa"`, `p = "*"`
  - **Output**: `true`
  - **Explanation**: `'*'` matches any sequence.

- **Example 3**:
  - **Input**: `s = "cb"`, `p = "?a"`
  - **Output**: `false`
  - **Explanation**: `'?` matches 'c', but the second letter is 'a', which does not match 'b'.

### Constraints

- `0 <= s.length, p.length <= 2000`
- `s` contains only lowercase English letters.
- `p` contains only lowercase English letters, `?` or `*`.

### Solution

The algorithm follows these steps:

1. **Initialize Pointers**: Start with two pointers, one for the string `s` and one for the pattern `p`. Additionally, maintain a variable to track the last position of any wildcard (`*`) encountered.

2. **Iterate Through String**: Use a loop to iterate through each character of the string `s`:
   - If the current character in `p` is a wildcard `*`, record the position and continue.
   - If the characters match or the current character in `p` is `?`, move both pointers forward.
   - If there is a mismatch and a `*` has been encountered previously, backtrack to the last `*` and try to match the remaining characters of `s` again.

3. **Final Matching**: After exiting the loop, check if there are any remaining characters in the pattern `p`. If there are unmatched `*` at the end of `p`, they can be ignored, allowing for a successful match.

4. **Return Result**: The final result will be `true` if all characters in both `s` and `p` are matched correctly, otherwise return `false`.

### Complexity Analysis

- **Time Complexity**: Average O(m + n), worst-case O(m · n) due to backtracking.
- **Space Complexity**: O(1) extra space.

### Python Reference

See `wildcard-matching.py` for the greedy backtracking implementation.

### Conclusion

This algorithm efficiently solves the wildcard matching problem by leveraging the properties of wildcards and backtracking when necessary, ensuring that the entire string matches the pattern as specified.
