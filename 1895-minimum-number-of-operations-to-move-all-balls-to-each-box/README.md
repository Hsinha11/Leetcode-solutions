<h2><a href="https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box">Minimum Number of Operations to Move All Balls to Each Box</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>You have <code>n</code> boxes. You are given a binary string <code>boxes</code> of length <code>n</code>, where <code>boxes[i]</code> is <code>&#39;0&#39;</code> if the <code>i<sup>th</sup></code> box is <strong>empty</strong>, and <code>&#39;1&#39;</code> if it contains <strong>one</strong> ball.</p>

<p>In one operation, you can move <strong>one</strong> ball from a box to an adjacent box. Box <code>i</code> is adjacent to box <code>j</code> if <code>abs(i - j) == 1</code>. Note that after doing so, there may be more than one ball in some boxes.</p>

<p>Return an array <code>answer</code> of size <code>n</code>, where <code>answer[i]</code> is the <strong>minimum</strong> number of operations needed to move all the balls to the <code>i<sup>th</sup></code> box.</p>

<p>Each <code>answer[i]</code> is calculated considering the <strong>initial</strong> state of the boxes.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> boxes = &quot;110&quot;
<strong>Output:</strong> [1,1,3]
<strong>Explanation:</strong> The answer for each box is as follows:
1) First box: you will have to move one ball from the second box to the first box in one operation.
2) Second box: you will have to move one ball from the first box to the second box in one operation.
3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> boxes = &quot;001011&quot;
<strong>Output:</strong> [11,8,5,4,3,4]</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == boxes.length</code></li>
	<li><code>1 &lt;= n &lt;= 2000</code></li>
	<li><code>boxes[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
</ul>

<hr/>

<h3>Approach</h3>
<p>
We can compute the minimum operations for each position in two linear passes using prefix sums:
</p>
<ul>
  <li>
    Left-to-right: maintain <code>balls_on_left</code> (how many balls seen so far) and <code>moves_from_left</code> (total cost to move those balls to current index). At each index <code>i</code>, add <code>moves_from_left</code> to the answer, then update the counters.
  </li>
  <li>
    Right-to-left: similarly maintain <code>balls_on_right</code> and <code>moves_from_right</code>, and add to the answer for each index.
  </li>
</ul>
<p>
This works because moving each ball by one step adds exactly one to the cost, and the two passes independently account for contributions from balls on each side.
</p>

<h3>Complexity</h3>
<ul>
  <li><strong>Time:</strong> <code>O(n)</code> — two linear passes.</li>
  <li><strong>Space:</strong> <code>O(n)</code> for the output array, <code>O(1)</code> extra space.</li>
</ul>

<h3>Reference Implementation (Python)</h3>

```python
from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result: List[int] = [0] * n

        balls_on_left = 0
        moves_from_left = 0
        for i in range(n):
            result[i] += moves_from_left
            if boxes[i] == '1':
                balls_on_left += 1
            moves_from_left += balls_on_left

        balls_on_right = 0
        moves_from_right = 0
        for i in range(n - 1, -1, -1):
            result[i] += moves_from_right
            if boxes[i] == '1':
                balls_on_right += 1
            moves_from_right += balls_on_right

        return result
```
