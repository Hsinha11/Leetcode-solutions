### 3709. Design Exam Scores Tracker

**Approach:**  
Use two arrays to store times and prefix sums of scores. Since insertions happen in strictly increasing time order, prefix sums allow fast cumulative score calculation. For each totalScore query, binary search is used to find the range and compute the difference of prefix sums.

**Complexity:**  
- Time: O(1) for record, O(log n) for totalScore query  
- Space: O(n)
