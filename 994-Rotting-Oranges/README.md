# 994 - Rotting Oranges

## Difficulty:
Medium

## Programming Language Used:
C++

## Problem Statement
You are given an <b> m x n </b> grid where each cell can have one of three values:  
- 0 representing an empty cell,  
- 1 representing a fresh orange, or 
- 2 representing a rotten orange.  

Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.  

Return <b> the minimum number of minutes that must elapse until no cell has a fresh orange.</b>  
If it is impossible, return <b>-1</b>.

**Example 1:**
```text
grid = [
  [2,1,1],
  [1,1,0],
  [0,1,1]
]
```



**Output:**
``` bash 
4
```

**Input 2 :**

```bash
grid = [
  [2,1,1],
  [0,1,1],
  [1,0,1]]
]
```

**Output :**
``` bash 
-1
```

**Output 3 :**

```bash
grid = [[0,2]]
```
**Output :**
``` bash 
0
```


**Constraints:**
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10
- grid[i][j] is 0, 1, or 2.

## Approach

We use a multi-source BFS (Breadth-First Search) because rotten oranges rot adjacent fresh oranges simultaneously per minute.

Steps:

- Initialize a queue with all initially rotten oranges.
- Count all fresh oranges.
- Perform BFS level by level:
  1. Each level represents 1 minute.
  2. For each rotten orange in the current level, rot all adjacent fresh oranges and add them to the queue.
  3. Decrement the count of fresh oranges.

- Continue until the queue is empty.
- If any fresh orange remains, return -1. Otherwise, return the number of minutes elapsed.

## Time and Space Complexity

- Time Complexity: <b>O(R × C)</b> (Each cell is visited at most once during BFS.)
- Space Complexity: <b>O(R × C)</b> (In the worst case, all oranges could be in the queue simultaneously.)

## Example 

Input Grid:
```bash 
[2,1,1]
[1,1,0]
[0,1,1]
```
Step By Step for Multi Source BFS

- Minute 0: Initial rotten orange positions (0,0)

``` bash
2 1 1
1 1 0
0 1 1
```
- Minute 1: Oranges adjacent to (0,0) become rotten

``` bash
2 2 1
2 1 0
0 1 1
```

- Minute 2: Newly rotten oranges rot their neighbors
``` bash
2 2 2
2 2 0
0 1 1
```

- Minute 3: Next round of adjacent oranges rot
```bash
2 2 2
2 2 0
0 2 1
```
- Minute 4: All oranges are rotten
```bash
2 2 2
2 2 0
0 2 2
```
Output : <b> 4 </b> minutes

##





