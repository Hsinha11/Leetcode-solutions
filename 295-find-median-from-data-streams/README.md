### 295. Find Median from Data Stream

**Approach:**  
Use two heaps to maintain the lower and upper halves of the data. The max-heap stores the smaller half, and the min-heap stores the larger half. The heaps are balanced such that their sizes differ by at most one. This structure allows constant-time median retrieval and logarithmic-time insertion.

**Complexity:**  
- Time: O(log n) per insertion, O(1) for median retrieval  
- Space: O(n)
