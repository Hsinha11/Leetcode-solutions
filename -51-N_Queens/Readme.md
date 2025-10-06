# 🧩 Problem: N-Queens

## 📘 Problem Statement
**Problem Link:** [https://leetcode.com/problems/n-queens/description/](https://leetcode.com/problems/n-queens/description/)

The N-Queens puzzle is the problem of placing `n` chess queens on an `n x n` chessboard so that no two queens attack each other.

A queen can attack another queen if they share the same row, column, or diagonal.

You need to return **all distinct solutions** to the N-Queens puzzle. Each solution contains a distinct board configuration, where `'Q'` represents a queen and `'.'` represents an empty space.

---

## 🧮 Example

### Input:
n = 4

### Output:
[
[".Q..",
"...Q",
"Q...",
"..Q."],

["..Q.",
"Q...",
"...Q",
".Q.."]
]

### Explanation:
There exist two distinct solutions for placing 4 queens on a 4×4 board.

---

## 🧠 Approach

We solve this problem using **Backtracking**:

1. Place one queen per column, starting from the leftmost column.
2. For each column, try placing the queen in all possible rows.
3. Before placing, check if the position is **safe** (no queens in same row, upper diagonal, or lower diagonal on the left side).
4. If placing a queen is valid, recursively place queens in the next column.
5. If all columns are filled, record the current board configuration as one valid solution.
6. Backtrack (remove the last queen) and continue exploring other possibilities.

---

## ⚙️ Complexity

- **Time Complexity:** `O(N!)`  
  Each queen has at most N choices, and constraints reduce combinations drastically through backtracking.

- **Space Complexity:** `O(N^2)`  
  Due to the recursion stack and the board storage for each configuration.

---

## 🧩 Example Code (C++ / Java / Python)

Each version uses the same recursive backtracking logic for solving the N-Queens problem.

- ✅ **C++:** Uses vectors and recursion  
- ✅ **Java:** Uses lists and 2D arrays  
- ✅ **Python:** Uses nested lists and strings  

---

## 🎯 Summary

- Uses **recursive backtracking** to explore all valid configurations.
- Prunes invalid states early using `isSafe` checks.
- Collects all unique board arrangements that satisfy N-Queens conditions.

---
