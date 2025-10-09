## [Triangle](https://leetcode.com/problems/triangle)
![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

<hr>
<p>
Given a <code>triangle</code> array, return the minimum path sum from top to bottom.
</p>
<p>
For each step, you may move to an adjacent number of the row below. More formally, if you are on index <code>i</code> on the current row, you may move to either index <code>i</code> or index <code>i + 1</code> on the next row.
</p>

### Example 1:
<pre>
<strong>Input:</strong> triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
<strong>Output:</strong> 11
<strong>Explanation:</strong> The minimum path sum is 2 + 3 + 5 + 1 = 11.
</pre>

### Constraints:
- <code>1 &lt;= triangle.length &lt;= 200</code>
- <code>triangle[0].length == 1</code>
- <code>triangle[i].length == i + 1</code>
- <code>-10<sup>4</sup> &lt;= triangle[i][j] &lt;= 10<sup>4</sup></code>
