# 🧩 Sliding Window Maximum

## 📘 Problem Statement
You are given an array of integers `nums`. There is a sliding window of size `k` which moves from the very left of the array to the very right.  
You can only see the `k` numbers inside the window at a time.  
Each time the sliding window moves right by one position.  

Return the **maximum** value in each sliding window.


---

## 💡 Approach — Using Deque (Double-Ended Queue)

To efficiently find the maximum element in each window, we use a **monotonic deque** — a deque that keeps elements in decreasing order of their values.

### Key Ideas:
1. The deque stores **indices**, not elements.
2. The **front of the deque** always holds the index of the **maximum element** in the current window.
3. For each element:
   - Remove elements smaller than the current number from the **back**.
   - Remove indices from the **front** if they are out of the current window range.
   - Once we have processed `k` elements, record the element at the **front** as the current maximum.

---

## 🧠 Algorithm Steps
1. Initialize:
   - A deque `q` to store useful element indices.
   - Two pointers `l` and `r` representing window boundaries.
   - A list `output` to store maximum values for each window.

2. Traverse through `nums` using `r`:
   - While `q` is not empty and `nums[q[-1]] < nums[r]`, pop from the back of the deque.
   - Append `r` to `q`.
   - If the left pointer `l` moves past `q[0]`, pop from the front.
   - Once the window reaches size `k`, append `nums[q[0]]` to the output list and increment `l`.

3. Return `output` after the loop ends.

---

## 🧾 Code Implementation
```python
import collections

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        output = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            # Remove elements smaller than the current one
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # Remove elements outside the window
            if l > q[0]:
                q.popleft()

            # Add the max element of the current window
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1
        return output

---

## ⏱️ Time & Space Complexity Analysis

### Time Complexity: **O(n)**
- **Main Loop**: We iterate through the array once with the right pointer `r`, which takes O(n) time.
- **Deque Operations**: Each element is added to the deque exactly once and removed at most once.
  - `q.append(r)`: O(1) per operation
  - `q.pop()`: O(1) per operation, executed at most n times total
  - `q.popleft()`: O(1) per operation, executed at most n times total
- **Overall**: Since each element is processed at most twice (once added, once removed), the total time complexity is **O(n)**.

### Space Complexity: **O(k)**
- **Deque Storage**: The deque can contain at most `k` elements at any time (one for each position in the sliding window).
- **Output Array**: The output array stores `n-k+1` elements (number of sliding windows).
- **Overall**: The dominant factor is the deque size, giving us **O(k)** space complexity.

### Why This is Optimal:
- **Naive Approach**: For each window, scan all k elements to find the maximum → O(nk) time.
- **Our Approach**: Using a monotonic deque allows us to find the maximum in O(1) time per window → O(n) time.
- **Trade-off**: We use O(k) extra space to achieve O(n) time instead of O(nk).

