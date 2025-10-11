## LeetCode 118: Pascal's Triangle

### Problem Link
- https://leetcode.com/problems/pascals-triangle/

### Solutions Available
- `pascals_triangle.py` — Python
- `pascals_triangle.cpp` — C++

### Approach
- Build row by row; first and last elements are `1`.
- Inner elements are sum of two elements above: `row[c] = prev[c-1] + prev[c]`.

### Complexity
- Time: `O(numRows^2)`
- Space: `O(numRows^2)` for the triangle (each row stored)

