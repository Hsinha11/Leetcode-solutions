<h2><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii">Best Time to Buy and Sell Stock III</a></h2> <img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' /><hr><p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p>

<p>Find the maximum profit you can achieve. You may complete <strong>at most two transactions</strong>.</p>

<p><strong>Note:</strong> You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> prices = [3,3,5,0,0,3,1,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> prices = [1,2,3,4,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> prices = [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transaction is done, i.e. max profit = 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= prices[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<hr/>

<h3>Approach</h3>
<p>
Use a 2-transaction state machine tracked in O(1) space:
Maintain <code>buy1</code>, <code>profit1</code>, <code>buy2</code>, <code>profit2</code>. For each price:
<code>buy1 = min(buy1, price)</code>, <code>profit1 = max(profit1, price - buy1)</code>,
<code>buy2 = min(buy2, price - profit1)</code>, <code>profit2 = max(profit2, price - buy2)</code>.
The final answer is <code>profit2</code>.
</p>

<h3>Complexity</h3>
<ul>
  <li><strong>Time:</strong> <code>O(n)</code></li>
  <li><strong>Space:</strong> <code>O(1)</code></li>
</ul>

<h3>Reference Implementation (Python)</h3>

```python
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = buy2 = float('inf')
        profit1 = profit2 = 0

        for price in prices:
            buy1 = min(buy1, price)
            profit1 = max(profit1, price - buy1)
            buy2 = min(buy2, price - profit1)
            profit2 = max(profit2, price - buy2)

        return profit2
```
