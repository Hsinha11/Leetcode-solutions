### 2076. Process Restricted Friend Requests

**Approach:**  
Use Union-Find (DSU) to maintain friend groups. For each friend request, we simulate the merge and check if merging the two users would cause any restricted pair to end up in the same connected component. If so, we reject the request; otherwise, we accept and perform the union.

**Complexity:**  
- Time: O(R * α(N) + Q * R)  
- Space: O(N)
