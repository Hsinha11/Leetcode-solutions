<h2><a href="https://leetcode.com/problems/maximum-total-beauty-of-gardens">Maximum Total Beauty of Gardens</a></h2> 
<img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />
<hr>

<p>
Alice is a caretaker of <code>n</code> gardens and she wants to plant flowers to maximize the total beauty of all her gardens.
</p>

<p>
You are given:
</p>
<ul>
  <li>A 0-indexed integer array <code>flowers</code> of size <code>n</code>, where <code>flowers[i]</code> is the number of flowers already planted in the <code>i<sup>th</sup></code> garden. Flowers that are already planted cannot be removed.</li>
  <li>An integer <code>newFlowers</code>, which is the maximum number of flowers Alice can additionally plant.</li>
  <li>Integers <code>target</code>, <code>full</code>, and <code>partial</code>.</li>
</ul>

<p>
A garden is considered <strong>complete</strong> if it has at least <code>target</code> flowers.  
The total beauty of the gardens is then determined as the sum of the following:
</p>
<ul>
  <li>The number of complete gardens multiplied by <code>full</code>.</li>
  <li>The minimum number of flowers in any of the incomplete gardens multiplied by <code>partial</code>. If there are no incomplete gardens, then this value is <code>0</code>.</li>
</ul>

<p>
Return <em>the maximum total beauty</em> that Alice can obtain after planting at most <code>newFlowers</code> flowers.
</p>

---

### Example 1:
```text
Input: flowers = [1,3,1,1], newFlowers = 7, target = 6, full = 12, partial = 1
Output: 14
Explanation:
Alice can plant:
- 2 flowers in the 0th garden
- 3 flowers in the 1st garden
- 1 flower in the 2nd garden
- 1 flower in the 3rd garden
The gardens become [3,6,2,2].
Complete gardens = 1 (garden 1)
Minimum flowers in incomplete gardens = 2
Total beauty = 1*12 + 2*1 = 14
