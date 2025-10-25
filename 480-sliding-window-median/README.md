### 480. Sliding Window Median

**Approach:**  
Use two heaps (max-heap for left half, min-heap for right half) to maintain window elements and find median efficiently. Rebalance heaps as window slides.

**Complexity:**  
- Time: O(n log k)  
- Space: O(k)
