## [4Sum](https://leetcode.com/problems/4sum)
![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

<hr>
<p>Given an array <code>nums</code> of <code>n</code> integers, return all the <strong>unique</strong> quadruplets <code>[nums[a], nums[b], nums[c], nums[d]]</code> such that:</p>
<ul>
  <li><code>0 &lt;= a, b, c, d &lt; n</code></li>
  <li><code>a</code>, <code>b</code>, <code>c</code>, and <code>d</code> are distinct.</li>
  <li><code>nums[a] + nums[b] + nums[c] + nums[d] == target</code></li>
</ul>

### Example 1:
<pre>
<strong>Input:</strong> nums = [1,0,-1,0,-2,2], target = 0
<strong>Output:</strong> [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
</pre>

### Constraints:
- <code>1 &lt;= nums.length &lt;= 200</code>
- <code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code>
- <code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code>
