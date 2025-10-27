### 3347-maximum-frequency-of-an-element-after-performing-operations-ii

**Approach:** Sort nums; for each distinct value v, count elements in [v-k, v+k] and compute achievable frequency using up to numOperations.  
**Complexity:** Time O(n log n), Space O(n)
