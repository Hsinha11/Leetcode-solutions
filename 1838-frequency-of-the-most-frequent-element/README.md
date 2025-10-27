### 1838. Frequency of the Most Frequent Element

**Approach:**  
Sort the array and use a sliding window. Make all elements in the window equal to the rightmost. Track increments needed and shrink window if it exceeds k. Maximize window size.

**Complexity:**  
- Time: O(n log n)  
- Space: O(1) extra (O(n) if counting sort)
