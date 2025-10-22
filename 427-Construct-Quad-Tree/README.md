# 🧩 Construct QuadTree from Grid

This project implements a **QuadTree construction algorithm** from a binary 2D grid using **Depth-First Search (DFS)**.  
A QuadTree is a tree data structure in which each internal node has exactly four children — commonly used for image compression, spatial indexing, and matrix decomposition.

---

## 🚀 Problem Description

Given a **binary grid** (2D list of 0s and 1s), construct a **QuadTree** where:

- Each node represents a square region of the grid.
- If all the cells in a region have the same value (`0` or `1`), it becomes a **leaf node**.
- Otherwise, the region is subdivided into **four equal quadrants**:
  - Top Left  
  - Top Right  
  - Bottom Left  
  - Bottom Right

---

## 🧱 Code Implementation

```python
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution(object):
    def construct(self, grid):
        def dfs(n, r, c):
            allsame = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r+i][c+j]:
                        allsame = False
                        break
                if not allsame:
                    break
            if allsame:
                return Node(grid[r][c], True)
            n //= 2
            topleft = dfs(n, r, c)
            topright = dfs(n, r, c+n)
            bottomleft = dfs(n, r+n, c)
            bottomright = dfs(n, r+n, c+n)
            return Node(0, False, topleft, topright, bottomleft, bottomright)

        return dfs(len(grid), 0, 0)


# Helper function to print the QuadTree structure
def printQuadTree(node, level=0):
    if not node:
        return
    indent = " " * (4 * level)
    print(f"{indent}Node(val={node.val}, isLeaf={node.isLeaf})")
    if not node.isLeaf:
        printQuadTree(node.topLeft, level + 1)
        printQuadTree(node.topRight, level + 1)
        printQuadTree(node.bottomLeft, level + 1)
        printQuadTree(node.bottomRight, level + 1)


# Example Test Case
if __name__ == "__main__":
    grid = [
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1]
    ]

    sol = Solution()
    root = sol.construct(grid)

    print("Constructed QuadTree:")
    printQuadTree(root)


#time complexity : O(N^2logN) ->Each recursive call checks up to N² cells and divides the grid into 4 quadrants. Recursion depth is log N.
#space complexity : O(N^2) -> In the worst case (no uniform regions), a node is created for almost every cell.