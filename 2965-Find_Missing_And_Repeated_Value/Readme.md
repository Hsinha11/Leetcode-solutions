# 📌 Problem: 2965. Find Missing and Repeated Values

## 📚 Problem Statement
You are given a 0-indexed 2D integer matrix `grid` of size `n x n` with values in the range `[1, n²]`. Each integer appears exactly once except:

- One number `a` appears twice
- One number `b` is missing

Your task is to find the repeated and missing numbers.

## 🛠️ Constraints
- `n == grid.length == grid[i].length`
- `2 <= n <= 50`
- `1 <= grid[i][j] <= n * n`

## 🌟 Examples

### Example 1
```
Input: grid = [[1,3],[2,2]]
Output: [2,4]
Explanation: 
- Number 2 is repeated
- Number 4 is missing
```

### Example 2
```
Input: grid = [[9,1,7],[8,9,2],[3,4,6]]
Output: [9,5]
Explanation: 
- Number 9 is repeated
- Number 5 is missing
```

## 🚀 Approach

### Algorithm
1. **Flatten the 2D matrix** and count occurrences of each number from 1 to n² using a frequency array
2. **Loop through the frequency array**:
   - If a number's count is 2, it is the repeated number `a`
   - If a number's count is 0, it is the missing number `b`

### Key Insights
- Since we know the range is [1, n²] and only one number is missing and one is repeated, we can use a simple counting approach
- The frequency array approach is straightforward and efficient for this problem size

## 🔧 Time & Space Complexity
- **Time Complexity**: O(n²) - We iterate through the entire grid once
- **Space Complexity**: O(n²) - For the count array of size n² + 1

## 💡 Solution Code
```python
class Solution:
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        size = n * n
        count = [0] * (size + 1)
        
        # Count occurrences of each number
        for i in range(n):
            for j in range(n):
                count[grid[i][j]] += 1
        
        a = b = -1
        # Find repeated and missing numbers
        for num in range(1, size + 1):
            if count[num] == 2:
                a = num
            elif count[num] == 0:
                b = num
        
        return [a, b]
```

