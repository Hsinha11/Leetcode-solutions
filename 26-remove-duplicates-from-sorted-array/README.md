# 26. Remove Duplicates from Sorted Array

## Problem Statement

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates **in-place** such that each unique element appears only **once**. The **relative order** of the elements should be kept the **same**. Then return *the number of unique elements in* `nums`.

Consider the number of unique elements of `nums` to be `k`, to get accepted, you need to do the following things:

- Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially. The remaining elements of `nums` are not important as well as the size of `nums`.
- Return `k`.

### Custom Judge:

The judge will test your solution with the following code:

```
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

If all assertions pass, then your solution will be **accepted**.

### Example 1:
```
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

### Example 2:
```
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

### Constraints:
- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in **non-decreasing** order.

---

## Approach

### Two Pointers Technique

This problem can be efficiently solved using the **Two Pointers** approach:

1. **Initialization**: 
   - Use a pointer `k` to track the position where the next unique element should be placed
   - Start with `k = 1` (since the first element is always unique)

2. **Iteration**:
   - Iterate through the array starting from index 1
   - Compare each element with the previous element (`nums[i]` vs `nums[i-1]`)
   - If they are different, we found a new unique element:
     - Place it at position `k`
     - Increment `k`

3. **Return**:
   - Return `k`, which represents the count of unique elements

### Why This Works:
- Since the array is **already sorted**, all duplicate elements are adjacent
- We only need to compare consecutive elements to identify duplicates
- By using the `k` pointer, we efficiently overwrite duplicates in-place
- We don't need extra space beyond the input array

### Visual Example:
```
Input: [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

Step-by-step:
k=1, i=1: nums[1]=0 == nums[0]=0 → skip
k=1, i=2: nums[2]=1 != nums[1]=0 → nums[k]=1, k=2
k=2, i=3: nums[3]=1 == nums[2]=1 → skip
k=2, i=4: nums[4]=1 == nums[3]=1 → skip
k=2, i=5: nums[5]=2 != nums[4]=1 → nums[k]=2, k=3
k=3, i=6: nums[6]=2 == nums[5]=2 → skip
k=3, i=7: nums[7]=3 != nums[6]=2 → nums[k]=3, k=4
k=3, i=8: nums[8]=3 == nums[7]=3 → skip
k=4, i=9: nums[9]=4 != nums[8]=3 → nums[k]=4, k=5

Result: [0, 1, 2, 3, 4, _, _, _, _, _], k=5
```

---

## Complexity Analysis

### Time Complexity: **O(n)**
- We iterate through the array exactly once
- Each element is visited once
- Comparison and assignment operations are O(1)
- Overall: **O(n)** where n is the length of the array

### Space Complexity: **O(1)**
- We only use two pointers (`k` and `i`)
- No additional data structures are used
- Modifications are done **in-place**
- Overall: **O(1)** constant extra space

---

## Key Insights

✅ **In-place modification**: The problem requires modifying the array without using extra space

✅ **Sorted array advantage**: Since the array is sorted, duplicates are always adjacent

✅ **Two pointers pattern**: Classic use case for the two-pointer technique

✅ **Relative order preserved**: The order of unique elements remains the same as in the original array

✅ **Optimal solution**: This is the most efficient approach with O(n) time and O(1) space

---

## Tags
- **Array**
- **Two Pointers**
- **Easy**
- **In-place Algorithm**

---

## Related Problems
- 27. Remove Element
- 80. Remove Duplicates from Sorted Array II
- 283. Move Zeroes
