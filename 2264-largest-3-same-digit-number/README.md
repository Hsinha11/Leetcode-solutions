# 2264. Largest 3-Same-Digit Number in String

## Problem Description

You are given a string `num` representing a large integer. A **good integer** is defined as a substring of `num` having length 3 that consists of only one unique digit. Return the **maximum good integer** as a string or an empty string `""` if no such integer exists.

Note that:
- A **substring** is a contiguous sequence of characters within a string.
- There may be **leading zeros** in `num` or a good integer.

### Example 1:
```
Input: num = "6777133339"
Output: "777"
Explanation: There are two distinct good integers: "777" and "333".
"777" is the largest, so we return "777".
```

### Example 2:
```
Input: num = "2300019"
Output: "000"
Explanation: "000" is the only good integer.
```

### Example 3:
```
Input: num = "42352338"
Output: ""
Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.
```

### Constraints:
* 3 <= num.length <= 1000
* num only consists of digits.

## Approach

The solution uses a sliding window approach to find the largest substring of length 3 with identical digits.

### Algorithm:
1. Initialize a variable `maxDigit` to track the largest digit that forms a good integer
2. Iterate through the string with a window of size 3
3. For each window:
   - Check if all three digits are the same
   - If yes, update `maxDigit` if current digit is larger
4. After the iteration:
   - If `maxDigit` was found, return a string with three copies of it
   - Otherwise, return empty string

### Time and Space Complexity:
- Time Complexity: O(n), where n is the length of the string
- Space Complexity: O(1), as we only use a fixed amount of space

## Why this Approach Works

1. By checking consecutive triplets of digits, we ensure we find all possible good integers
2. By tracking only the maximum digit that forms a good integer, we ensure we find the largest good integer
3. Using the string constructor with repeat count efficiently creates the result

## Implementation Details

The solution uses:
- Sliding window technique for substring checking
- `string(count, char)` constructor for creating the result string
- Character comparison for finding identical digits
- `max()` function to track the largest valid digit found