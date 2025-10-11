# 349. Intersection of Two Arrays

## Problem Statement:
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

## Example 1:
**Input:** nums1 = [1,2,2,1], nums2 = [2,2]
**Output:** [2]

## Example 1:
**Input:** nums1 = [4,9,5], nums2 = [9,4,9,8,4]
**Output:** [9,4] ([4,9] is also accepted.)

**Constraints**
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000


## Approach
1. Sort `nums1` and `nums2` arrays.
2. Create a pointer for each array, initially set to 0.
3. Initialize an empty set that stores intersecting integers.
4. If the integers at both pointers equal the same value, add this value to the intersecting set and increment both pointers.
5. Otherwise, increment the pointer that points to the smaller integer value.
6. Repeat steps 4 and 5 until a pointer is out of bounds.
7. Convert the intersection set into an array.
8. Return the resulting array.

## Complexity
- **Time:** O(nlogn+mlogm)
- **Space:** O(min(m,n))
