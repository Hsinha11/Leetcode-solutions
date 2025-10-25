### 3691-maximum-total-subarray-value-ii

**Approach:** Enumerate top-k subarray values using RMQ + max-heap enumeration (or use editorial O((n+k) log n) method with monotonic stacks + heap). Extract k largest (max - min) for subarrays and sum them.  
**Complexity:** Time O((n + k) log n) (heap enumeration with O(1) RMQ per extraction), Space O(n).
