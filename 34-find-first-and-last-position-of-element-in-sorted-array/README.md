## 34. Find First and Last Position of Element in Sorted Array

**Difficulty:** Medium  
**Link:** [LeetCode 34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

---

### Approach
Use **two binary searches**:
1. Find the **first occurrence** (leftmost index) of target.
2. Find the **last occurrence** (rightmost index) of target.  
This ensures O(log n) runtime as required.

---

### Complexity
- **Time Complexity:** O(log n)  
- **Space Complexity:** O(1)
