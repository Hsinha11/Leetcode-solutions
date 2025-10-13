# Minimum Pair Removal to Make Array Non-Decreasing

## Problem Statement
Given an array of integers `nums`, you can perform the following operation any number of times:
- Select the **adjacent pair with the minimum sum** in `nums`. If multiple such pairs exist, choose the **leftmost** one.
- Replace the pair with their sum.

Return the **minimum number of operations** needed to make the array **non-decreasing**.
An array is non-decreasing if each element is greater than or equal to its previous element.

---

## Approach
1. **Check non-decreasing**: Use a helper function `isNonDecreasing()` to check if the array is already non-decreasing.
2. **Find and merge minimum sum pair**: 
   - Iterate through the array to find the **leftmost adjacent pair with the minimum sum**.
   - Merge this pair into a single element (sum of the pair) and form a new array.
3. Repeat steps 1 and 2 until the array becomes non-decreasing.
4. Count each merge operation to get the **minimum number of operations**.

---

## Time and Space Complexity

- **Time Complexity**:  
  - `isNonDecreasing` takes `O(n)`  
  - `mergeMinSumPair` takes `O(n)`  
  - Worst-case scenario: roughly `O(n^2)` because we may perform up to `n-1` merges.
- **Space Complexity**: `O(n)` for creating a new array at each merge.

---

## Example Walkthrough

**Input:**  

nums = [5, 3, 2, 4]

- Step 1: Find leftmost min sum pair: [3, 2] → sum = 5
- New array: [5, 5, 4]

- Step 2: Find leftmost min sum pair: [5, 4] → sum = 9
- New array: [5, 9]

- Step 3: Array is now non-decreasing → stop

**Output:**
operations = 2
