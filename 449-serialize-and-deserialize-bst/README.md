<h2><a href="https://leetcode.com/problems/serialize-and-deserialize-bst">Serialize and Deserialize BST</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.</p>

<p>Design an algorithm to serialize and deserialize a <b>binary search tree</b>. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.</p>

<p><b>The encoded string should be as compact as possible.</b></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> root = [2,1,3]
<strong>Output:</strong> [2,1,3]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
	<li>The input tree is <strong>guaranteed</strong> to be a binary search tree.</li>
</ul>

<hr/>

<h3>Approach</h3>
<p>
We serialize the BST using <strong>preorder traversal</strong> (root-left-right), storing only the values as a compact space-separated string. To deserialize, we consume the preorder sequence while enforcing <strong>BST bounds</strong> (<code>min</code>, <code>max</code>) for each subtree. Each value belongs to exactly one interval and is used once, which reconstructs the original BST in linear time.
</p>

<h4>Steps</h4>
<ol>
  <li><strong>Serialize:</strong> Do a preorder DFS and append node values; join by spaces.</li>
  <li><strong>Deserialize:</strong> Build the tree by reading values in order and recursing with bounds:
    <ul>
      <li>Left subtree allowed range: <code>(min, root.val)</code></li>
      <li>Right subtree allowed range: <code>(root.val, max)</code></li>
    </ul>
  </li>
</ol>

<h4>Complexity</h4>
<ul>
  <li><strong>Time:</strong> <code>O(n)</code> for both serialize and deserialize.</li>
  <li><strong>Space:</strong> <code>O(n)</code> for output and recursion stack in the worst case.</li>
</ul>

<h4>Python Reference</h4>
<p>See <code>serialize-and-deserialize-bst.py</code> in this folder.</p>