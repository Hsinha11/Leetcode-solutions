### 1202. Smallest String With Swaps

**Approach:**  
Use a Disjoint Set Union (Union-Find) to group indices that can be swapped. Each connected component represents indices that can reach each other via swaps. For each component, extract the indices and the characters at those indices, sort both, and reassign the smallest characters to the smallest indices to get the lexicographically smallest result.

**Complexity:**  
- Time: O(n log n + m α(n))  
- Space: O(n)
