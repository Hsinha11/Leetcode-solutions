# 1906. Minimum Absolute Difference Queries

## Problem

Given an array `nums` and queries `[l, r]`, return for each query the minimum absolute difference between two distinct elements in `nums[l..r]`. If the subarray contains fewer than two distinct values, return `-1`.

Key constraint: `1 <= nums[i] <= 100`.

## Intuition

Because values lie in `[1..100]`, we can precompute prefix frequency counts. For any query range, we can quickly know which values appear, then the minimum difference must be between consecutive distinct values in sorted order.

## Approach

1. Build `prefix[i][v]` = count of value `v` in `nums[:i]` for all `v` in `1..100`.
2. For each query `[l, r]`:
   - For each `v` in `1..100`, compute `cnt = prefix[r+1][v] - prefix[l][v]`.
   - Track consecutive present values to compute the minimum gap.
   - If fewer than two distinct values appear, return `-1`.

## Complexity

- Preprocessing: O(n \* 100)
- Per query: O(100)
- Total: O(n*100 + q*100) with small constant factor (100).

## Edge Cases

- Single-element subarray → `-1`
- All elements equal in range → `-1`
- Duplicates do not affect the gap; only distinct values matter.

## Example

nums = [1,3,4,8]
queries = [[0,1],[1,2],[2,3],[0,3]]
output = [2,1,4,1]
