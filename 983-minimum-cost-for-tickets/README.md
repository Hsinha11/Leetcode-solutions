<h2><a href="https://leetcode.com/problems/minimum-add-to-make-parentheses-valid">921. Minimum Add to Make Parentheses Valid</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

<hr>

<p>A parentheses string is valid if and only if:</p>

<ul>
	<li>It is the empty string,</li>
	<li>It can be written as <code>AB</code> (<code>A</code> concatenated with <code>B</code>), where <code>A</code> and <code>B</code> are valid strings, or</li>
	<li>It can be written as <code>(A)</code>, where <code>A</code> is a valid string.</li>
</ul>

<p>You are given a parentheses string <code>s</code>. In one move, you can insert a parenthesis at any position of the string.</p>

<ul>
	<li>For example, if <code>s = "()))"</code>, you can insert an opening parenthesis to be <code>"((()))"</code> or a closing parenthesis to be <code>"())))"</code>.</li>
</ul>

<p>Return <em>the minimum number of moves required to make </em><code>s</code><em> valid</em>.</p>

<hr>

<h3>Example 1:</h3>

<pre>
<strong>Input:</strong> s = "())"
<strong>Output:</strong> 1
</pre>

<h3>Example 2:</h3>

<pre>
<strong>Input:</strong> s = "((("
<strong>Output:</strong> 3
</pre>

<h3>Example 3:</h3>

<pre>
<strong>Input:</strong> s = "()"
<strong>Output:</strong> 0
</pre>

<h3>Example 4:</h3>

<pre>
<strong>Input:</strong> s = "()))(("
<strong>Output:</strong> 4
</pre>

<hr>

<h2>🧠 Approach</h2>

<p>We can count how many opening and closing parentheses are unmatched while iterating through the string.</p>

<ul>
	<li>Whenever we see an opening bracket <code>(</code>, we increment <code>open_count</code>.</li>
	<li>Whenever we see a closing bracket <code>)</code>:
		<ul>
			<li>If <code>open_count &gt; 0</code>, we can match it with a previous opening one (so decrement <code>open_count</code>).</li>
			<li>Otherwise, it means we need to insert one opening bracket, so increment <code>insertions</code>.</li>
		</ul>
	</li>
</ul>

<p>At the end, <code>open_count</code> represents unmatched opening brackets, and <code>insertions</code> represents unmatched closing brackets.</p>

<p>The answer is <code>open_count + insertions</code>.</p>

<hr>

<h2>⏱️ Complexity</h2>

<ul>
	<li><b>Time Complexity:</b> O(N) — We iterate once through the string.</li>
	<li><b>Space Complexity:</b> O(1) — We only use counters.</li>
</ul>

<hr>

<h2>💻 Code Implementation (Python)</h2>

```python
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """
        Returns the minimum number of parentheses additions
        required to make the string valid.
        """
        open_count = 0   # Tracks unmatched '('
        insertions = 0   # Tracks unmatched ')'

        for ch in s:
            if ch == '(':
                open_count += 1
            else:  # ch == ')'
                if open_count > 0:
                    open_count -= 1  # Match with existing '('
                else:
                    insertions += 1  # Need one '(' to match

        # Remaining open_count are unmatched '('
        return open_count + insertions
