<h2><a href="https://leetcode.com/problems/maximum-performance-of-a-team">Maximum Performance of a Team</a></h2> 
<img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />
<hr>

<p>
You are given two integers <code>n</code> and <code>k</code> and two integer arrays <code>speed</code> and <code>efficiency</code> both of length <code>n</code>, where <code>speed[i]</code> and <code>efficiency[i]</code> represent the speed and efficiency of the <code>i<sup>th</sup></code> engineer respectively.
</p>

<p>
Choose at most <code>k</code> different engineers out of the <code>n</code> engineers to form a team with the maximum performance.
</p>

<p>
The performance of a team is defined as the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.
</p>

<p>
Return <em>the maximum performance of this team</em> modulo <code>10<sup>9</sup> + 7</code>.
</p>

---

### Example 1:
```text
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60
Explanation:
We select engineer 2 (speed=10, efficiency=4) and engineer 5 (speed=5, efficiency=7).
Team performance = (10 + 5) * min(4,7) = 15 * 4 = 60.