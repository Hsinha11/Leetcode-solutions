# 283. Move Zeroes

## Problem Statement

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

**Note**: You must do this **in-place** without making a copy of the array.

### Example 1:
```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```

### Example 2:
```
Input: nums = [0]
Output: [0]
```

### Constraints:
- `1 <= nums.length <= 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

**Follow-up**: Could you minimize the total number of operations done?

---

## Approach

### Two Pointers Technique (Optimal Solution)

This problem can be elegantly solved using the **Two Pointers** approach with a single pass:

1. **Initialization**: 
   - Use a pointer `left` to track the position where the next non-zero element should be placed
   - Start with `left = 0`

2. **Single Pass Iteration**:
   - Iterate through the array with pointer `right`
   - When `nums[right]` is non-zero:
     - Swap `nums[left]` with `nums[right]`
     - Increment `left` pointer
   - This effectively moves all non-zero elements to the front

3. **Result**:
   - All non-zero elements are moved to the front in their original order
   - All zeros naturally end up at the back

### Why This Works:
- **In-place**: No extra space needed beyond two pointers
- **Maintains order**: Non-zero elements preserve their relative positions
- **Efficient**: Single pass through the array with O(n) time
- **Minimizes operations**: Only swaps when necessary

### Visual Example:
```
Input: [0, 1, 0, 3, 12]

Initial: left=0, right=0
        [0, 1, 0, 3, 12]
         ↑
         L,R

Step 1: nums[0]=0 (zero), skip
        left=0, right=1
        [0, 1, 0, 3, 12]
         ↑  ↑
         L  R

Step 2: nums[1]=1 (non-zero), swap(0,1)
        left=1, right=2
        [1, 0, 0, 3, 12]
            ↑  ↑
            L  R

Step 3: nums[2]=0 (zero), skip
        left=1, right=3
        [1, 0, 0, 3, 12]
            ↑     ↑
            L     R

Step 4: nums[3]=3 (non-zero), swap(1,3)
        left=2, right=4
        [1, 3, 0, 0, 12]
               ↑     ↑
               L     R

Step 5: nums[4]=12 (non-zero), swap(2,4)
        left=3, right=5
        [1, 3, 12, 0, 0]
                  ↑
                  L

Result: [1, 3, 12, 0, 0] ✓
```

### Alternative Approaches:

**Approach 2: Two-Pass Solution**
1. First pass: Move all non-zero elements to the front
2. Second pass: Fill remaining positions with zeros
- Time: O(n), Space: O(1)
- More operations than optimal solution

**Approach 3: Using Extra Space (Not Optimal)**
- Create new array, copy non-zeros first, then zeros
- Time: O(n), Space: O(n)
- Violates in-place requirement

---

## Complexity Analysis

### Time Complexity: **O(n)**
- Single pass through the array
- Each element is visited once
- Swap operation is O(1)
- Overall: **O(n)** where n is the length of the array

### Space Complexity: **O(1)**
- Only two pointers (`left` and `right`) are used
- No additional data structures
- All operations are done **in-place**
- Overall: **O(1)** constant extra space

---

## Key Insights

✅ **Two pointers pattern**: Classic application of the two-pointer technique

✅ **In-place swap**: Efficiently rearranges elements without extra space

✅ **Order preservation**: Non-zero elements maintain their relative order

✅ **Single pass**: Optimal solution with minimal operations

✅ **Stable algorithm**: The relative order of non-zero elements is preserved

✅ **Follow-up satisfied**: Minimizes total operations by using swaps only when needed

---

## Edge Cases

- **All zeros**: `[0, 0, 0]` → `[0, 0, 0]`
- **No zeros**: `[1, 2, 3]` → `[1, 2, 3]`
- **Single element**: `[0]` or `[5]` → remains unchanged
- **Zeros at end**: `[1, 2, 0, 0]` → `[1, 2, 0, 0]` (already in correct position)
- **Zeros at start**: `[0, 0, 1, 2]` → `[1, 2, 0, 0]`

---

## Tags
- **Array**
- **Two Pointers**
- **Easy**
- **In-place Algorithm**

---

## Related Problems
- 26. Remove Duplicates from Sorted Array
- 27. Remove Element
- 80. Remove Duplicates from Sorted Array II
- 75. Sort Colors
