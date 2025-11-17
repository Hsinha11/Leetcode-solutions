<h2><a href="https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii">Minimum Moves to Equal Array Elements III</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>You are given an integer array <code>nums</code>.</p>

<p>In one move, you may <strong>increase</strong> the value of any single element <code>nums[i]</code> by 1.</p>

<p>Return the <strong>minimum total</strong> number of <strong>moves</strong> required so that all elements in <code>nums</code> become <strong>equal</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,1,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>To make all elements equal:</p>

<ul>
	<li>Increase <code>nums[0] = 2</code> by 1 to make it 3.</li>
	<li>Increase <code>nums[1] = 1</code> by 1 to make it 2.</li>
	<li>Increase <code>nums[1] = 2</code> by 1 to make it 3.</li>
</ul>

<p>Now, all elements of <code>nums</code> are equal to 3. The minimum total moves is <code>3</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,4,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>To make all elements equal:</p>

<ul>
	<li>Increase <code>nums[0] = 4</code> by 1 to make it 5.</li>
	<li>Increase <code>nums[1] = 4</code> by 1 to make it 5.</li>
</ul>

<p>Now, all elements of <code>nums</code> are equal to 5. The minimum total moves is <code>2</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>
