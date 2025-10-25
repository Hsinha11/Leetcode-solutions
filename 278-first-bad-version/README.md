## 278. First Bad Version

**Difficulty:** Easy  
**Link:** [LeetCode 278. First Bad Version](https://leetcode.com/problems/first-bad-version/)

---

### Approach
We use **binary search** to find the first version that fails the quality check.  
At each step, we check the middle version:
- If it's bad, the first bad version is at or before `mid`.
- Otherwise, it lies after `mid`.  
This minimizes the number of API calls.

---

### Complexity
- **Time Complexity:** O(log n)  
- **Space Complexity:** O(1)
