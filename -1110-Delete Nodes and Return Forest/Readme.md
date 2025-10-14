
## Delete Nodes and Return Forest

**Difficulty:** Medium

A binary tree is given along with a list of node values to delete. When a node is deleted, its children become new roots (if they are not deleted themselves).
Return the forest (list of remaining tree roots) after deleting all specified nodes.

### Example 1:

**Input:**
root = [1,2,3,4,5,6,7], to_delete = [3,5]

**Output:**
[[1,2,null,4],[6],[7]]

**Explanation:**
Nodes 3 and 5 are deleted. The remaining trees are rooted at 1, 6, and 7.

### Constraints:

* The number of nodes in the tree is in the range **[1, 1000]**
* **0 <= Node.val <= 1000**
* All values in `to_delete` are unique and within the node value range

**Time Complexity:** O(n)
**Space Complexity:** O(n)
