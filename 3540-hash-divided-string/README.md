<h2><a href="https://leetcode.com/problems/hash-divided-string">Hash Divided String</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>You are given a string <code>s</code> of length <code>n</code> and an integer <code>k</code>, where <code>n</code> is a <strong>multiple</strong> of <code>k</code>. Your task is to hash the string <code>s</code> into a new string called <code>result</code>, which has a length of <code>n / k</code>.</p>

<p>First, divide <code>s</code> into <code>n / k</code> <strong><span data-keyword="substring-nonempty">substrings</span></strong>, each with a length of <code>k</code>. Then, initialize <code>result</code> as an <strong>empty</strong> string.</p>

<p>For each <strong>substring</strong> in order from the beginning:</p>

<ul>
	<li>The <strong>hash value</strong> of a character is the index of that characte<!-- notionvc: 4b67483a-fa95-40b6-870d-2eacd9bc18d8 -->r in the <strong>English alphabet</strong> (e.g., <code>&#39;a&#39; &rarr;<!-- notionvc: d3f8e4c2-23cd-41ad-a14b-101dfe4c5aba --> 0</code>, <code>&#39;b&#39; &rarr;<!-- notionvc: d3f8e4c2-23cd-41ad-a14b-101dfe4c5aba --> 1</code>, ..., <code>&#39;z&#39; &rarr;<!-- notionvc: d3f8e4c2-23cd-41ad-a14b-101dfe4c5aba --> 25</code>).</li>
	<li>Calculate the <em>sum</em> of all the <strong>hash values</strong> of the characters in the substring.</li>
	<li>Find the remainder of this sum when divided by 26, which is called <code>hashedChar</code>.</li>
	<li>Identify the character in the English lowercase alphabet that corresponds to <code>hashedChar</code>.</li>
	<li>Append that character to the end of <code>result</code>.</li>
</ul>

<p>Return <code>result</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abcd&quot;, k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;bf&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>First substring: <code>&quot;ab&quot;</code>, <code>0 + 1 = 1</code>, <code>1 % 26 = 1</code>, <code>result[0] = &#39;b&#39;</code>.</p>

<p>Second substring: <code>&quot;cd&quot;</code>, <code>2 + 3 = 5</code>, <code>5 % 26 = 5</code>, <code>result[1] = &#39;f&#39;</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;mxz&quot;, k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;i&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>The only substring: <code>&quot;mxz&quot;</code>, <code>12 + 23 + 25 = 60</code>, <code>60 % 26 = 8</code>, <code>result[0] = &#39;i&#39;</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 100</code></li>
	<li><code>k &lt;= s.length &lt;= 1000</code></li>
	<li><code>s.length</code> is divisible by <code>k</code>.</li>
	<li><code>s</code> consists only of lowercase English letters.</li>
</ul>
