<h2><a href="https://leetcode.com/problems/score-validator">Score Validator</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>You are given a string array <code>events</code>.</p>

<p>Initially, <code>score = 0</code> and <code>counter = 0</code>. Each element in <code>events</code> is one of the following:</p>

<ul>
	<li><code>&quot;0&quot;</code>, <code>&quot;1&quot;</code>, <code>&quot;2&quot;</code>, <code>&quot;3&quot;</code>, <code>&quot;4&quot;</code>, <code>&quot;6&quot;</code>: Add that value to the total score.</li>
	<li><code>&quot;W&quot;</code>: Increase the counter by 1. No score is added.</li>
	<li><code>&quot;WD&quot;</code>: Add 1 to the total score.</li>
	<li><code>&quot;NB&quot;</code>: Add 1 to the total score.</li>
</ul>

<p>Process the array from left to right. Stop processing when either:</p>

<ul>
	<li>All elements in <code>events</code> have been processed, or</li>
	<li>The counter becomes 10.</li>
</ul>

<p>Return an integer array <code>[score, counter]</code>, where:</p>

<ul>
	<li><code>score</code> is the final total score.</li>
	<li><code>counter</code> is the final counter value.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">events = [&quot;1&quot;,&quot;4&quot;,&quot;W&quot;,&quot;6&quot;,&quot;WD&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[12,1]</span></p>

<p><strong>Explanation:</strong></p>

<table>
	<tbody>
		<tr>
			<th>Event</th>
			<th>Score</th>
			<th>Counter</th>
		</tr>
		<tr>
			<td><code>&quot;1&quot;</code></td>
			<td>1</td>
			<td>0</td>
		</tr>
		<tr>
			<td><code>&quot;4&quot;</code></td>
			<td>5</td>
			<td>0</td>
		</tr>
		<tr>
			<td><code>&quot;W&quot;</code></td>
			<td>5</td>
			<td>1</td>
		</tr>
		<tr>
			<td><code>&quot;6&quot;</code></td>
			<td>11</td>
			<td>1</td>
		</tr>
		<tr>
			<td><code>&quot;WD&quot;</code></td>
			<td>12</td>
			<td>1</td>
		</tr>
	</tbody>
</table>

<p>Final result: <code>[12, 1]</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">events = [&quot;WD&quot;,&quot;NB&quot;,&quot;0&quot;,&quot;4&quot;,&quot;4&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[10,0]</span></p>

<p><strong>Explanation:</strong></p>

<table>
	<tbody>
		<tr>
			<th>Event</th>
			<th>Score</th>
			<th>Counter</th>
		</tr>
		<tr>
			<td><code>&quot;WD&quot;</code></td>
			<td>1</td>
			<td>0</td>
		</tr>
		<tr>
			<td><code>&quot;NB&quot;</code></td>
			<td>2</td>
			<td>0</td>
		</tr>
		<tr>
			<td><code>&quot;0&quot;</code></td>
			<td>2</td>
			<td>0</td>
		</tr>
		<tr>
			<td><code>&quot;4&quot;</code></td>
			<td>6</td>
			<td>0</td>
		</tr>
		<tr>
			<td><code>&quot;4&quot;</code></td>
			<td>10</td>
			<td>0</td>
		</tr>
	</tbody>
</table>

<p>Final result: <code>[10, 0]</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">events = [&quot;W&quot;,&quot;W&quot;,&quot;W&quot;,&quot;W&quot;,&quot;W&quot;,&quot;W&quot;,&quot;W&quot;,&quot;W&quot;,&quot;W&quot;,&quot;W&quot;,&quot;W&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,10]</span></p>

<p><strong>Explanation:</strong></p>

<p>After 10 occurrences of <code>&quot;W&quot;</code>, the counter reaches 10, so processing stops. The remaining events are ignored.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= events.length &lt;= 1000</code></li>
	<li><code>events[i]</code> is one of <code>&quot;0&quot;</code>, <code>&quot;1&quot;</code>, <code>&quot;2&quot;</code>, <code>&quot;3&quot;</code>, <code>&quot;4&quot;</code>, <code>&quot;6&quot;</code>, <code>&quot;W&quot;</code>, <code>&quot;WD&quot;</code>, or <code>&quot;NB&quot;</code>.</li>
</ul>
