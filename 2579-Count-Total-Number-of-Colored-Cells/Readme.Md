<h2><a href="https://leetcode.com/problems/count-total-number-of-colored-cells">2579. Count Total Number of Colored Cells</a></h2>
<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />
<hr>

<p>There exists an infinitely large two-dimensional grid of uncolored unit cells. You are given a positive integer <code>n</code>, denoting the number of steps to be taken.</p>

<p>In each step <code>i (1 ≤ i ≤ n)</code>, a cell is chosen, and all cells that are at a <strong>Manhattan distance</strong> of <code>i - 1</code> from that cell are colored.</p>

<p>Return the <strong>total number of colored cells</strong> after <code>n</code> steps.</p>

<hr>

<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 1</span></p>
<p><strong>Output:</strong> <span class="example-io">1</span></p>
<p><strong>Explanation:</strong></p>
<p>After step 1, only one cell is colored.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3</span></p>
<p><strong>Output:</strong> <span class="example-io">13</span></p>
<p><strong>Explanation:</strong></p>
<p>
At each step, the number of newly colored cells forms a diamond pattern:<br>
n = 1 → 1 cell<br>
n = 2 → 5 cells<br>
n = 3 → 13 cells<br>
Total = 13
</p>
</div>

<hr>

<h3>🧩 Approach</h3>

<p>
The pattern of colored cells forms a <strong>diamond shape</strong> that grows symmetrically.<br>
The total number of colored cells after <code>n</code> steps follows the formula:
</p>

<pre>
Total = 1 + 4 * (1 + 2 + 3 + ... + (n - 1))
</pre>

<p>
Using the sum of first <code>n-1</code> natural numbers, the formula simplifies to:
</p>

<pre>
Total = 1 + 4 * n * (n - 1) / 2
</pre>

<hr>

<hr> <h3>⏱️ Complexity Analysis</h3> <ul> <li><strong>Time Complexity:</strong> O(1)</li> <li><strong>Space Complexity:</strong> O(1)</li> </ul> <hr> <h3>📘 Intuition</h3> <p> Each step expands the diamond shape by adding four edges of length <code>n - 1</code> symmetrically around the center cell.<br> The formula <code>1 + 4 * n * (n - 1) / 2</code> directly computes the total number of colored cells without simulation. </p>
