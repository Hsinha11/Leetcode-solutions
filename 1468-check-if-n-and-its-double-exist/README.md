<h2><a href="https://leetcode.com/problems/check-if-n-and-its-double-exist">Check If N and Its Double Exist</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given an array <code>arr</code> of integers, check if there exist two indices <code>i</code> and <code>j</code> such that :</p>

<ul>
	<li><code>i != j</code></li>
	<li><code>0 &lt;= i, j &lt; arr.length</code></li>
	<li><code>arr[i] == 2 * arr[j]</code></li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [10,2,5,3]
<strong>Output:</strong> true
<strong>Explanation:</strong> For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [3,1,7,11]
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no i and j that satisfy the conditions.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= arr.length &lt;= 500</code></li>
	<li><code>-10<sup>3</sup> &lt;= arr[i] &lt;= 10<sup>3</sup></code></li>
</ul>

<h3>Approach</h3>
<p>
We iterate through the array while maintaining a hash structure of previously seen values.
For each current value <code>x</code>, we check:
</p>
<ul>
  <li>If <code>2 * x</code> exists among seen values, then the earlier value is double of <code>x</code>.</li>
  <li>If <code>x</code> is even and <code>x / 2</code> exists among seen values, then the earlier value is half of <code>x</code>.</li>
  <li>If either condition is true, return <code>true</code>. Otherwise, add <code>x</code> to the seen set and continue.</li>
  <li>This logic correctly handles zeros and negative values.</li>
  
</ul>

<h3>Complexity</h3>
<ul>
  <li><strong>Time</strong>: <code>O(n)</code> — each value is processed once with constant average-time lookups.</li>
  <li><strong>Space</strong>: <code>O(n)</code> — storing up to <code>n</code> seen values.</li>
</ul>
