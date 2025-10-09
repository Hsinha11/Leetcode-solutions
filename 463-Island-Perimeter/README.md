# LeetCode 463: Island Perimeter

## 🧩 Problem Description
You are given `grid`, where `grid[i][j] = 1` represents land and `grid[i][j] = 0` represents water.
A cell is part of the island if it’s connected 4-directionally (up, down, left, right) to another land cell.

**Return the perimeter of the island.**

### Example 1:
```
Input: grid = [
  [0,1,0,0],
  [1,1,1,0],
  [0,1,0,0],
  [1,1,0,0]
]
Output: 16
```

### Example 2:
```
Input: grid = [[1]]
Output: 4
```

### Constraints:
- 1 <= grid.length, grid[i].length <= 100
- grid[i][j] is either 0 or 1

---

## 💡 Approach
Each land cell contributes **4 sides** initially.
If it shares a border with another land cell (up or left), reduce **2** from the perimeter.

**Time Complexity:** O(N × M)  
**Space Complexity:** O(1)
