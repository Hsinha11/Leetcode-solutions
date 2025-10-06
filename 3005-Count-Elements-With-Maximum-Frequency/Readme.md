<h2><a href="https://leetcode.com/problems/count-elements-with-maximum-frequency">3005. Count Elements With Maximum Frequency</a></h2>
<img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy" />
<hr>

<p>Given an integer array <code>nums</code>, return the <strong>total number of elements</strong> that appear the <strong>maximum number of times</strong>.</p>

<hr>

<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,2,3,1,4]</span></p>
<p><strong>Output:</strong> <span class="example-io">4</span></p>
<p><strong>Explanation:</strong></p>
<p>The elements <code>1</code> and <code>2</code> both appear twice, which is the maximum frequency.<br>
Total count = 2 (from 1s) + 2 (from 2s) = 4.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4,5]</span></p>
<p><strong>Output:</strong> <span class="example-io">5</span></p>
<p><strong>Explanation:</strong></p>
<p>All elements appear once (max frequency = 1).<br>
Total count = 5.</p>
</div>

<hr>

<h3>🧩 Approach</h3>

<p>
1️⃣ Count how many times each element appears using <code>collections.Counter</code>.<br>
2️⃣ Find the maximum frequency among all elements.<br>
3️⃣ Sum up the counts of all elements that have this maximum frequency.
</p>

<hr>

<h3>🧾 Code Implementation (Python)</h3>

```python
from collections import Counter
from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = Counter(nums)
        max_freq = max(counts.values())
        return sum(freq for freq in counts.values() if freq == max_freq)
```
<hr> <h3>🧪 Example Run</h3>

```python
sol = Solution()
print(sol.maxFrequencyElements([1,2,2,3,1,4]))  # Output: 4
print(sol.maxFrequencyElements([1,2,3,4,5]))    # Output: 5
```

<hr> <h3>⏱️ Complexity Analysis</h3> <ul> <li><strong>Time Complexity:</strong> O(n)</li> <li><strong>Space Complexity:</strong> O(n)</li> </ul> <hr> <h3>📘 Intuition</h3> <p> Every element that appears the maximum number of times contributes fully to the count.<br> So if multiple elements share that same maximum frequency, we add them all together. </p>