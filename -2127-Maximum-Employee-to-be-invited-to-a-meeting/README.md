# LeetCode 2127: Maximum Number of Employees in a Meeting

## Problem Link
- [LeetCode 2127: Maximum Number of Employees in a Meeting](https://leetcode.com/problems/maximum-number-of-employees-in-a-meeting/)

## Solutions Available
- `Maximum_Employee.py` — Python
- `Maximum_Employee.cpp` — C++

## Approach (both implementations)
We treat `favorite[i]` as a directed graph where each node has out-degree 1.

- Detect and remove nodes not in any cycle using a queue on nodes with `indegree == 0`, computing the longest chain length feeding into each node.
- Remaining nodes form cycles. The answer is the maximum of:
  - The longest cycle length, and
  - The sum over all mutual pairs (2-cycles `a <-> b`) of `2 + depth[a] + depth[b]`.

## Complexity
- Time: `O(N)`
- Space: `O(N)`

## Notes
- The C++ file includes a small `main` for quick local testing; remove it for LeetCode submission or wrap with `#ifndef ONLINE_JUDGE` if preferred.