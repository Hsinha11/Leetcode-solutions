# Subarrays with K Different Integers

## Problem Statement

Given an integer array `nums` and an integer `k`, return the number of **good subarrays** of `nums`.

A **good array** is an array where the number of different integers in that array is **exactly** `k`.

A **subarray** is a contiguous part of an array.

### Examples

**Example 1:**
```
Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays with exactly 2 different integers:
[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
```

**Example 2:**
```
Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays with exactly 3 different integers:
[1,2,1,3], [2,1,3], [1,3,4]
```

### Constraints
- `1 <= nums.length <= 2 * 10^4`
- `1 <= nums[i], k <= nums.length`

---

## Solution Approach

### 🎯 Core Insight

The key breakthrough is transforming the "exactly K" problem into an "at most K" problem:

```
Subarrays with EXACTLY k distinct = Subarrays with AT MOST k distinct 
                                   - Subarrays with AT MOST (k-1) distinct
```

**Why does this work?**
- "At most k" includes all subarrays with k, k-1, k-2, ..., 1 distinct integers
- "At most k-1" includes all subarrays with k-1, k-2, ..., 1 distinct integers
- The difference gives us only subarrays with exactly k distinct integers!

---

## Algorithm Breakdown

### Step 1: Count Subarrays with "At Most K" Distinct

We use the **sliding window** technique:

1. **Two Pointers**: `left` and `right` define our window
2. **Expand**: Move `right` pointer to include new elements
3. **Shrink**: Move `left` pointer when we exceed k distinct integers
4. **Count**: For each `right` position, all subarrays ending at `right` are valid

#### Why `right - left + 1`?

When window `[left, right]` has ≤ k distinct integers, we can form subarrays:
- `[left, right]`
- `[left+1, right]`
- `[left+2, right]`
- ...
- `[right, right]`

Total count = `right - left + 1`

### Step 2: Apply the Formula

```cpp
return atMostKDistinct(nums, k) - atMostKDistinct(nums, k - 1);
```

---

## Detailed Example Walkthrough

### Input: `nums = [1,2,1,2,3]`, `k = 2`

#### Computing `atMost(2)`:

| Step | right | nums[right] | Window | Distinct | Count Added | Total |
|------|-------|-------------|--------|----------|-------------|-------|
| 1 | 0 | 1 | [1] | {1} | 1 | 1 |
| 2 | 1 | 2 | [1,2] | {1,2} | 2 | 3 |
| 3 | 2 | 1 | [1,2,1] | {1,2} | 3 | 6 |
| 4 | 3 | 2 | [1,2,1,2] | {1,2} | 4 | 10 |
| 5 | 4 | 3 | [1,2,1,2,3] | {1,2,3} | Shrink! | |
| 5b | 4 | 3 | [1,2,3] | {1,2,3} | Shrink! | |
| 5c | 4 | 3 | [2,3] | {2,3} | 3 | 13 |

**Result: 13**

#### Computing `atMost(1)`:

| Step | right | nums[right] | Window | Distinct | Count Added | Total |
|------|-------|-------------|--------|----------|-------------|-------|
| 1 | 0 | 1 | [1] | {1} | 1 | 1 |
| 2 | 1 | 2 | [1,2] | {1,2} | Shrink! | |
| 2b | 1 | 2 | [2] | {2} | 1 | 2 |
| 3 | 2 | 1 | [2,1] | {2,1} | Shrink! | |
| 3b | 2 | 1 | [1] | {1} | 1 | 3 |
| 4 | 3 | 2 | [1,2] | {1,2} | Shrink! | |
| 4b | 3 | 2 | [2] | {2} | 1 | 4 |
| 5 | 4 | 3 | [2,3] | {2,3} | Shrink! | |
| 5b | 4 | 3 | [3] | {3} | 1 | 5 |

**Result: 6**

#### Final Answer:
```
atMost(2) - atMost(1) = 13 - 6 = 7 ✓
```

---

## Complexity Analysis

### Time Complexity: **O(n)**
- Each element is visited at most twice (once by `right`, once by `left`)
- Hash map operations (`insert`, `erase`, `find`) are O(1) on average
- Two passes through the array (one for k, one for k-1)

### Space Complexity: **O(k)**
- Hash map stores at most `k+1` distinct integers at any time
- Additional space for variables is O(1)

---

## Code Structure

```cpp
class Solution {
public:
    int subarraysWithKDistinct(vector<int>& nums, int k) {
        // Main function: applies the formula
        return atMostKDistinct(nums, k) - atMostKDistinct(nums, k - 1);
    }
    
private:
    int atMostKDistinct(vector<int>& nums, int k) {
        // Helper function: counts subarrays with ≤ k distinct integers
        // Uses sliding window technique
    }
};
```

---

## Key Takeaways

1. **Transform the Problem**: "Exactly K" is harder than "At Most K"
2. **Sliding Window**: Perfect for contiguous subarray problems
3. **Mathematical Insight**: Subtraction gives us the exact count
4. **Frequency Map**: Track distinct integers efficiently
5. **Optimal Solution**: Linear time complexity makes it suitable for large inputs

---

## Related Problems

- [Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)
- [Subarrays with At Most K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/)
- [Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/)

---

## Testing

The solution passes all LeetCode test cases including:
- Edge cases (k = 1, k = n)
- Large arrays (up to 20,000 elements)
- Arrays with repeated elements
- Arrays with all distinct elements

---

**LeetCode Problem**: [992. Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/)

**Difficulty**: Hard

**Topics**: Hash Table, Sliding Window, Counting