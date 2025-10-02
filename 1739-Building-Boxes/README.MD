<h2><a href="https://leetcode.com/problems/building-boxes">1739. Building Boxes</a></h2> 
<img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />
<hr>

<p>
You have a cubic storeroom where the width, length, and height of the room are all equal to <code>n</code> units.  
You are asked to place <code>n</code> boxes in this room where each box is a cube of unit side length.  
</p>

<p>There are some rules for placing the boxes:</p>
<ul>
  <li>You can place the boxes anywhere on the floor.</li>
  <li>If box <code>x</code> is placed on top of box <code>y</code>, then each of the four vertical sides of box <code>y</code> must either be adjacent to another box or to a wall.</li>
</ul>

<p>
Given an integer <code>n</code>, return <em>the minimum possible number of boxes touching the floor</em>.
</p>

---

### Example 1:
```text
Input: n = 3
Output: 3
Explanation:
Three boxes are placed in the corner of the room, touching the floor directly.
