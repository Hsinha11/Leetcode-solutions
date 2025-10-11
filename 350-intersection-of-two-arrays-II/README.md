# 350. Intersection of Two Arrays - II

## Problem Statement:
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 
## Example 1:
**Input:** nums1 = [1,2,2,1], nums2 = [2,2]
**Output:** [2,2]

## Example 1:
**Input:** nums1 = [4,9,5], nums2 = [9,4,9,8,4]
**Output:** [9,4] ([4,9] is also accepted.)

**Constraints**
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

## Approach
1. Sort `nums1` and `nums2` arrays.
2. Initialize two pointers: i = 0, j = 0.
3.While i < len(nums1) and j < len(nums2):
     • If nums1[i] < nums2[j]: i += 1
     • Else if nums1[i] > nums2[j]: j += 1
     • Else: append nums1[i] to result; i += 1; j += 1
4. Return the result list.

## Complexity
- **Time:**O(MlogM + NlogN)
- **Space:** O(sorting)
