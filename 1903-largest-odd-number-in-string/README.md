# 1903. Largest Odd Number in String

## Problem Description

You are given a string `num` representing a large integer. Return the **largest-valued odd integer** (as a string) that is a substring of `num`, or an empty string `""` if no odd integer exists.

A **substring** is a contiguous sequence of characters within a string.

### Example 1:
```
Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
```

### Example 2:
```
Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".
```

### Example 3:
```
Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.
```

### Constraints:
* 1 <= num.length <= 10^5
* num only consists of digits and does not contain any leading zeros.

## Approach

The solution uses a key observation: for a number to be odd, its last digit must be odd. Also, if we want the largest possible odd number, we should keep as many digits as possible from the original number up to the rightmost odd digit.

### Algorithm:
1. Iterate through the string from right to left
2. For each digit:
   - Check if it's odd (digit % 2 == 1)
   - If odd, return the substring from index 0 to current position (inclusive)
3. If no odd digit found, return empty string

### Time and Space Complexity:
- Time Complexity: O(n), where n is the length of the string
- Space Complexity: O(1), as we only use a fixed amount of space regardless of input size

## Why this Approach Works

Consider that we want the largest possible odd number. The largest number we can form will always be a prefix of the original number (to maintain the place values). Therefore:

1. If the original number is odd, it's the answer (largest possible)
2. If not, we need to find the rightmost odd digit and take everything before it
3. If no odd digit exists, no odd number can be formed

## Implementation Details

The solution uses:
- String's `substr()` function for extracting the prefix
- Character to integer conversion ('0' subtraction) for checking odd/even