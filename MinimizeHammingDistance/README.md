# 1722. Minimize Hamming Distance After Swap Operations

## 🧩 Problem Description
You are given two arrays `source` and `target`, and a list of index pairs `allowedSwaps`. You may perform unlimited swaps on `source` using these pairs. Each swap connects indices, and transitive connections form components where any index can be swapped with any other within that group.

### 🎯 Objective
Find the **minimum Hamming distance** between `source` and `target`, where Hamming distance is defined as positions where `source[i] != target[i]`.

---

## ✅ Approach (Union-Find / Disjoint Set Union)
1. Use DSU to group indices that can be swapped.
2. For each connected component:
   - Count frequencies of values in `source` and `target`.
   - The mismatches are the values that cannot be paired.

---

## 💻 Example
```cpp
source = [5,1,2,4,3]
target = [1,5,4,2,3]
allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]
Output: 0
