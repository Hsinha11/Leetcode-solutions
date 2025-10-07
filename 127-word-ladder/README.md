# 127. Word Ladder

Given two words `beginWord` and `endWord` and a dictionary `wordList`, return the length of the shortest transformation sequence from `beginWord` to `endWord` such that:
- Only one letter can be changed at a time.
- Each transformed word must exist in `wordList`.

If no sequence exists, return `0`.

## 🧠 Thought Process & Approach

We seek the shortest number of transformations, which is a classic shortest path problem on an implicit graph:
- Each word is a node.
- An edge exists between two words if they differ by exactly one letter.

Instead of checking all pairs (which is expensive), we build wildcard patterns to quickly find neighbors:
- Replace each position with `*` (e.g., "hot" → `*ot`, `h*t`, `ho*`) and map these to words sharing that pattern.
- Perform BFS from `beginWord`. The first time we reach `endWord`, we have the shortest path length.

Key points:
- Use a set for `wordList` to allow O(1) membership checks.
- Precompute pattern → words adjacency to avoid O(N^2) neighbor checks.
- Mark visited words to prevent revisiting.
- Optional optimization: clear the pattern list after processing to reduce repeated neighbor scans.

## 🔍 Algorithm

1. If `endWord` is not in `wordList`, return `0`.
2. Preprocess `wordList` into a dictionary from wildcard pattern to list of words.
3. BFS queue holds `(word, steps)`, initialized with `(beginWord, 1)`.
4. For the current `word`, generate its `L` wildcard patterns. For each pattern, explore all mapped neighbors:
   - If a neighbor is unseen, mark visited and enqueue with `steps + 1`.
5. If we dequeue `endWord`, return `steps`. If BFS finishes, return `0`.

## ⏱️ Time & Space Complexity

- Preprocessing: O(N * L) to build wildcard patterns for N words of length L.
- BFS traversal: Each word and its patterns processed once → O(N * L).
- Total: O(N * L) time, O(N * L) space.

This is optimal for this formulation compared to naive O(N^2 * L) neighbor checking.

## 📚 Example

```
Input:
beginWord = "hit"
endWord   = "cog"
wordList  = ["hot","dot","dog","lot","log","cog"]

Output:
5

Explanation:
hit → hot → dot → dog → cog
```

```
Input:
beginWord = "hit"
endWord   = "cog"
wordList  = ["hot","dot","dog","lot","log"]

Output:
0  (endWord not present in the list)
```

## 🧩 Categories
- Graphs
- BFS
- Strings

## 🛠️ Notes
- This solution uses standard BFS with pattern indexing for efficiency.
- Works when `beginWord` is not in `wordList` (common in problem constraints).