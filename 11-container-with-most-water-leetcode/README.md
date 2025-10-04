# Container With Most Water

**Problem Link:** [LeetCode 11 - Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

### Problem Statement
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the ith line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

**Note:** The container cannot be slanted.

---

### Example 1
Input:  
`height = [1,8,6,2,5,4,8,3,7]`  
Output:  
`49`  
Explanation:  
The above vertical lines represent the array `[1,8,6,2,5,4,8,3,7]`. The maximum area of water the container can hold is `49`.

---

### Example 2
Input:  
`height = [1,1]`  
Output:  
`1`

---

### Constraints
- `n == height.length`  
- `2 <= n <= 10^5`  
- `0 <= height[i] <= 10^4`

---

### Approach
- Use a **two-pointer technique**:
  - Initialize two pointers `lp = 0` and `rp = n - 1`.
  - Calculate the area formed between them.
  - Move the pointer pointing to the shorter line inward, as it limits the height of the container.
  - Continue until the two pointers meet.
- This approach ensures an optimal O(n) time complexity.

---

### Complexity
- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)
