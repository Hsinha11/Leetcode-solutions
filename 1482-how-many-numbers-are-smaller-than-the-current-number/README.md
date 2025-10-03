<h2><a href="https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number">How Many Numbers Are Smaller Than the Current Number</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given the array <code>nums</code>, for each <code>nums[i]</code> find out how many numbers in the array are smaller than it. That is, for each <code>nums[i]</code> you have to count the number of valid <code>j&#39;s</code>&nbsp;such that&nbsp;<code>j != i</code> <strong>and</strong> <code>nums[j] &lt; nums[i]</code>.</p>

<p>Return the answer in an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [8,1,2,2,3]
<strong>Output:</strong> [4,0,1,1,3]
<strong>Explanation:</strong> 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [6,5,4,8]
<strong>Output:</strong> [2,1,0,3]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [7,7,7,7]
<strong>Output:</strong> [0,0,0,0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 500</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
</ul>

<h3>Approach</h3>
<p>
Two common strategies:
</p>
<ul>
  <li><strong>Counting Sort (O(n))</strong>: Since <code>0 \le nums[i] \le 100</code>, count frequencies in an array of size 101, build prefix sums, and map each value to the count of strictly smaller numbers.</li>
  <li><strong>Sorting (O(n log n))</strong>: Copy and sort the array; the first index of each value equals how many numbers are smaller.</li>
  
</ul>

<h3>Complexity</h3>
<ul>
  <li><strong>Counting Sort</strong>: Time <code>O(n)</code>, Space <code>O(1)</code> extra (since 101 is constant).</li>
  <li><strong>Sorting</strong>: Time <code>O(n \log n)</code>, Space <code>O(n)</code>.</li>
</ul>
