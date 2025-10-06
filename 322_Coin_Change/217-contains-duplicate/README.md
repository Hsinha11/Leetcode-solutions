# 217. Contains Duplicate

**Problem Statement:**  
Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

**LeetCode Link:** [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

---

## Approach

We can solve this efficiently using a **hash set** (`unordered_set` in C++).  

1. Initialize an empty hash set `seen`.  
2. Iterate through each element `num` in `nums`:  
   - If `num` is already in `seen`, return `true` (duplicate found).  
   - Otherwise, insert `num` into `seen`.  
3. If the loop finishes without finding duplicates, return `false`.

This approach ensures we **check duplicates in O(1) time per element**.

---

## Time and Space Complexity

- **Time Complexity:** `O(n)` — we traverse the array once.  
- **Space Complexity:** `O(n)` — in the worst case, we store all `n` elements in the set.

---

## Example

**Example 1:**  
Input: `nums = [1,2,3,1]`  
Output: `true`  
Explanation: `1` appears twice.

**Example 2:**  
Input: `nums = [1,2,3,4]`  
Output: `false`  
Explanation: All elements are distinct.

**Example 3:**  
Input: `nums = [1,1,1,3,3,4,3,2,4,2]`  
Output: `true`  
Explanation: Multiple duplicates exist (`1, 3, 4, 2`).

---

## Notes
- This solution works for large arrays efficiently.
- Uses hash set for fast look-up.
