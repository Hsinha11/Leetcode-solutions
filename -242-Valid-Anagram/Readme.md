## LeetCode 242: Valid Anagram

### Problem Link
- [LeetCode 242: Valid Anagram](https://leetcode.com/problems/valid-anagram/)

### Solutions Available
- `-242-Valid_Anagram.py` — Python
- `Valid_Anagram.cpp` — C++

### Approach
- If lengths differ, return false immediately.
- Count characters of `s` and decrement with characters of `t` using fixed-size array of length 26 (lowercase assumption).
- If any count goes negative, not an anagram.

### Complexity
- Time: `O(n)`
- Space: `O(1)` (26-sized array)