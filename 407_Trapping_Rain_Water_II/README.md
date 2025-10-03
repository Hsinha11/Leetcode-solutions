# 407. Trapping Rain Water II

**Difficulty:** Hard  
**Topics:** Priority Queue, BFS, Matrix  

## Problem Statement

Given an `m x n` integer matrix `heightMap` representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

### Example 1

**Input:**  
```

heightMap = [[1,4,3,1,3,2],
[3,2,1,3,2,4],
[2,3,3,2,3,1]]

```

**Output:**  
```

4

```

**Explanation:**  
After the rain, water is trapped between the blocks.  
We have two small ponds with 1 and 3 units trapped.  
Total trapped water = 4.

### Example 2

**Input:**  
```

heightMap = [[3,3,3,3,3],
[3,2,2,2,3],
[3,2,1,2,3],
[3,2,2,2,3],
[3,3,3,3,3]]

```

**Output:**  
```

10

```

## Constraints

- `m == heightMap.length`  
- `n == heightMap[i].length`  
- `1 <= m, n <= 200`  
- `0 <= heightMap[i][j] <= 2 * 10^4`  

## Approach

1. Use a **priority queue (min-heap)** to process the lowest boundary first.
2. Apply **BFS** from the boundaries to the interior cells.
3. Maintain a **visited matrix** to avoid revisiting cells.
4. Water trapped in a cell = `max(0, height of surrounding boundary - height of cell)`.

## Solution

- Optimized with a complexity of `O(m * n * log(m * n))`.
- Includes solutions in **C++** and **Java**.
- Code is commented for clarity and understanding.

## Notes

- Make sure the matrix has at least 3 rows and 3 columns; otherwise, no water can be trapped.
- The approach ensures correct water trapping calculation even with uneven boundaries.
```
