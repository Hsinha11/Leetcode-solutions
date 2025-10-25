### 778. Swim in Rising Water

**Approach:**  
Use a priority queue (Min-Heap) to perform a Dijkstra-style traversal. At each step, we move to the adjacent cell with the smallest elevation possible and track the maximum elevation encountered on the path. The answer is the minimum time at which the target cell becomes reachable.

**Complexity:**  
- Time: O(n² log n)  
- Space: O(n²)
