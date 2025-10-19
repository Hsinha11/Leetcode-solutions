# 1493. Longest Subarray of 1's After Deleting One Element

## Status
**Solved**  
**Difficulty:** Medium  
**Languages:** Python, C++

## Description
Given a binary array `nums`, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

## Examples

### Example 1
**Input:** `nums = [1,1,0,1]`  
**Output:** `3`  
**Explanation:** After deleting the number in position 2, `[1,1,1]` contains 3 numbers with value of 1's.

### Example 2
**Input:** `nums = [0,1,1,1,0,1,1,0,1]`  
**Output:** `5`  
**Explanation:** After deleting the number in position 4, `[0,1,1,1,1,1,0,1]` longest subarray with value of 1's is `[1,1,1,1,1]`.

### Example 3
**Input:** `nums = [1,1,1]`  
**Output:** `2`  
**Explanation:** You must delete one element.

## Constraints
- `1 <= nums.length <= 10^5`
- `nums[i]` is either 0 or 1.

## Topics
- Array
- Sliding Window
- Two Pointers

## Companies
- [List of relevant companies]

## Solution Approach

### Algorithm
This problem uses a **sliding window** technique with two pointers:
1. **Expand Window**: Move right pointer to include new elements
2. **Count Zeros**: Track the number of zeros in the current window
3. **Shrink Window**: If more than one zero exists, move left pointer until at most one zero remains
4. **Update Result**: Calculate window length (minus 1 for deletion) and update maximum

### Key Insights
- We can delete at most one element (zero) from the array
- The longest subarray of 1's will be the window with at most one zero
- After deletion, the window length becomes `right - left` (since we delete one element)

### Complexity Analysis
- **Time Complexity**: O(n) - Each element is visited at most twice
- **Space Complexity**: O(1) - Only using constant extra space

## Solution Files
- `longest-subarray-of-1s-after-deleting-one -element.py` - Python implementation
- `longest-subarray-of-1s-after-deleting-one-element.cpp` - C++ implementation with test cases
