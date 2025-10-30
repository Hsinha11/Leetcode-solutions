# 35. Search Insert Positions

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 
## Example
Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

## Constraints

1 <= nums.length <= 104

-104 <= nums[i] <= 104

nums contains distinct values sorted in ascending order.

-104 <= target <= 104

## Approach

**Binary search** to locate the correct insertion point:

1. Initialize two pointers:  
   - `l = 0` (left boundary)  
   - `r = len(nums) - 1` (right boundary)
2. While `l <= r`:
   - Compute `mid = (l + r) // 2`
   - If `nums[mid] == target`: return `mid`
   - If `nums[mid] > target`: move `r = mid - 1`
   - Else: move `l = mid + 1`
3. When the loop ends, `l` points to the correct **insertion index**.