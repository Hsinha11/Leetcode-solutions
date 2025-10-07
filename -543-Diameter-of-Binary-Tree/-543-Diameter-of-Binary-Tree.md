# 543. Diameter of Binary Tree

> **Difficulty**: Easy  
> **Topics**: Tree, Depth-First Search, Binary Tree  
> **Time Complexity**: O(n)  
> **Space Complexity**: O(h) where h is height of tree

## 📋 Problem Statement

Given the `root` of a binary tree, return **the length of the diameter** of the tree.

The **diameter** of a binary tree is the **length of the longest path between any two nodes** in a tree. This path may or may not pass through the `root`.

The **length of a path** between two nodes is represented by the number of edges between them.

### Examples

#### Example 1:
```
          1
         / \
        2   3
       / \
      4   5

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
```

#### Example 2:
```
  1
 /
2

Input: root = [1,2]
Output: 1
```

### Constraints:
- The number of nodes in the tree is in the range `[1, 10^4]`
- `-100 <= Node.val <= 100`

---

## 🧠 Algorithm Explanation

### Core Concept: Height + Diameter Tracking

The key insight is that the diameter of a tree can be found by:

1. **For each node**, calculate the longest path that passes through it
2. **Track the maximum** diameter found across all nodes
3. **The longest path through a node** = left subtree height + right subtree height

### Visual Representation

```
        1        ← diameter through node 1 = 2 + 1 = 3
       / \
      2   3      ← diameter through node 2 = 1 + 1 = 2
     / \         ← diameter through node 3 = 0 + 0 = 0
    4   5       ← diameter through nodes 4,5 = 0 + 0 = 0

Heights: 4→0, 5→0, 2→1, 3→0, 1→2
Maximum diameter = 3 (path: 4→2→1→3 or 5→2→1→3)
```

### Algorithm Steps

1. **Recursive height calculation**: For each node, calculate subtree height
2. **Diameter update**: At each node, update global diameter = left_height + right_height
3. **Return height**: Return current subtree height for parent calculations
4. **Base case**: Empty nodes have height 0

---

## 💻 Implementation

### Python Solution

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        
        def height(node):
            if not node:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)
            
            # Update diameter: longest path through this node
            self.diameter = max(self.diameter, left_height + right_height)
            
            # Return height of subtree
            return 1 + max(left_height, right_height)
        
        height(root)
        return self.diameter


# -------- Example Usage --------
# Building the example tree: [1,2,3,4,5]
#         1
#        / \
#       2   3
#      / \
#     4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

sol = Solution()
print("Diameter of Binary Tree:", sol.diameterOfBinaryTree(root))  # Output: 3
```

### C++ Solution

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
private:
    int diameter = 0;
    
    int height(TreeNode* node) {
        if (!node) return 0;
        
        int leftHeight = height(node->left);
        int rightHeight = height(node->right);
        
        // Update diameter: longest path through this node
        diameter = max(diameter, leftHeight + rightHeight);
        
        // Return height of current subtree
        return 1 + max(leftHeight, rightHeight);
    }
    
public:
    int diameterOfBinaryTree(TreeNode* root) {
        diameter = 0;  // Reset for multiple calls
        height(root);
        return diameter;
    }
};

// Example usage
int main() {
    // Building tree: [1,2,3,4,5]
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    
    Solution sol;
    cout << "Diameter: " << sol.diameterOfBinaryTree(root) << endl;  // Output: 3
    
    return 0;
}
```

### Java Solution

```java
// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    private int diameter = 0;
    
    public int diameterOfBinaryTree(TreeNode root) {
        diameter = 0;  // Reset for multiple calls
        height(root);
        return diameter;
    }
    
    private int height(TreeNode node) {
        if (node == null) return 0;
        
        int leftHeight = height(node.left);
        int rightHeight = height(node.right);
        
        // Update diameter: longest path through this node
        diameter = Math.max(diameter, leftHeight + rightHeight);
        
        // Return height of current subtree
        return 1 + Math.max(leftHeight, rightHeight);
    }
}
```

---

## 🔍 Step-by-Step Walkthrough

### Example: Tree [1,2,3,4,5]

```
        1
       / \
      2   3
     / \
    4   5
```

| Node | Left Height | Right Height | Diameter Update | Height Returned |
|------|-------------|--------------|-----------------|-----------------|
| 4 | 0 | 0 | max(0, 0+0) = 0 | 1 |
| 5 | 0 | 0 | max(0, 0+0) = 0 | 1 |
| 2 | 1 | 1 | max(0, 1+1) = 2 | 2 |
| 3 | 0 | 0 | max(2, 0+0) = 2 | 1 |
| 1 | 2 | 1 | max(2, 2+1) = 3 | 3 |

**Final Result**: Diameter = **3**

### Execution Flow

1. **Start at root (1)**: Call height(1)
2. **Recurse left**: height(2) → height(4), height(5)
3. **Process leaf nodes**: 4 and 5 return height 1
4. **Process node 2**: diameter = 1 + 1 = 2, returns height 2
5. **Recurse right**: height(3) returns height 1
6. **Process root (1)**: diameter = 2 + 1 = 3, returns height 3

---

## 🎯 Key Insights

### 1. **Why This Approach Works**
- Every possible diameter path must pass through some node
- For each node, the longest path through it = left_height + right_height
- We check all nodes, so we find the maximum possible diameter

### 2. **Height vs Diameter**
```python
# Height: longest path from node to leaf (edges)
height = 1 + max(left_height, right_height)

# Diameter: longest path through node (edges)
diameter = left_height + right_height
```

### 3. **Edge Cases**
- **Single node**: diameter = 0 (no edges)
- **Linear tree**: diameter = n-1 (where n = number of nodes)
- **Empty tree**: diameter = 0

### 4. **Time Optimization**
- **Single pass**: Calculate height and diameter simultaneously
- **No redundant work**: Each node visited exactly once
- **Optimal complexity**: O(n) time, O(h) space

---

## 📊 Complexity Analysis

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| **DFS + Global Variable** | **O(n)** | **O(h)** | Optimal solution |
| Naive (check all paths) | O(n²) | O(h) | Inefficient |
| BFS + Path tracking | O(n²) | O(n) | Complex implementation |

**Where:**
- `n` = number of nodes
- `h` = height of tree (O(log n) balanced, O(n) skewed)

---

## 🧪 Test Cases

### Basic Cases
```python
# Test 1: Example tree
#     1
#    / \
#   2   3
#  / \
# 4   5
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
# Expected: 3

# Test 2: Linear tree
#   1
#  /
# 2
root = TreeNode(1, TreeNode(2), None)
# Expected: 1
```

### Edge Cases
```python
# Test 3: Single node
root = TreeNode(1)
# Expected: 0

# Test 4: Empty tree
root = None
# Expected: 0

# Test 5: Complete binary tree
#       1
#     /   \
#    2     3
#   / \   / \
#  4   5 6   7
# Expected: 4
```

### Advanced Cases
```python
# Test 6: Skewed tree (worst case)
#   1
#    \
#     2
#      \
#       3
#        \
#         4
# Expected: 3

# Test 7: Diameter not through root
#       1
#      /
#     2
#    / \
#   3   4
#  /   / \
# 5   6   7
# Expected: 4 (path: 5→3→2→4→6 or 5→3→2→4→7)
```

---

## 🚀 Alternative Approaches

### 1. **Return Tuple Approach** (Cleaner)

```python
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, 0  # (height, diameter)
            
            left_height, left_diameter = dfs(node.left)
            right_height, right_diameter = dfs(node.right)
            
            current_height = 1 + max(left_height, right_height)
            current_diameter = max(
                left_diameter,
                right_diameter,
                left_height + right_height
            )
            
            return current_height, current_diameter
        
        _, diameter = dfs(root)
        return diameter
```

### 2. **Class Variable Approach** (Thread-safe)

```python
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node, diameter_ref):
            if not node:
                return 0
            
            left = dfs(node.left, diameter_ref)
            right = dfs(node.right, diameter_ref)
            
            diameter_ref[0] = max(diameter_ref[0], left + right)
            return 1 + max(left, right)
        
        diameter = [0]
        dfs(root, diameter)
        return diameter[0]
```

---

## 📈 Performance Comparison

### Tree Types and Expected Performance

| Tree Type | Height | Time | Space | Diameter |
|-----------|--------|------|-------|----------|
| Balanced | O(log n) | O(n) | O(log n) | ~O(log n) |
| Skewed | O(n) | O(n) | O(n) | O(n) |
| Complete | O(log n) | O(n) | O(log n) | ~O(log n) |

---

## 💡 Tips for Interview

### Key Points to Mention:
1. **Problem understanding**: Diameter = longest path between any two nodes
2. **Key insight**: Path through node = left_height + right_height
3. **Optimization**: Calculate height and diameter in single pass
4. **Base cases**: Handle null nodes correctly

### Common Mistakes:
- Confusing diameter (edges) with number of nodes in path
- Forgetting to update diameter at each node
- Not handling empty trees
- Returning height instead of diameter

### Follow-up Questions:
- What if we want the actual path, not just length?
- How to handle very large trees (iterative solution)?
- What if tree nodes have weights?

---

## 🔧 Optimizations

### 1. **Memory Optimization**
```python
# Use iterative approach for very deep trees to avoid stack overflow
def diameterIterative(self, root):
    if not root:
        return 0
    
    stack = [(root, False)]
    heights = {None: 0}
    diameter = 0
    
    while stack:
        node, visited = stack.pop()
        if visited:
            left_h = heights[node.left]
            right_h = heights[node.right]
            heights[node] = 1 + max(left_h, right_h)
            diameter = max(diameter, left_h + right_h)
        else:
            stack.append((node, True))
            if node.left:
                stack.append((node.left, False))
            if node.right:
                stack.append((node.right, False))
    
    return diameter
```

### 2. **Early Termination** (for specific use cases)
```python
# If we only need to know if diameter exceeds a threshold
def diameterExceedsK(self, root, k):
    def dfs(node):
        if not node:
            return 0
        
        left = dfs(node.left)
        right = dfs(node.right)
        
        if left + right > k:
            return float('inf')  # Signal early termination
        
        return 1 + max(left, right)
    
    return dfs(root) == float('inf')
```

---

## 📚 Related Problems

### Similar Tree Problems:
- **[Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)** - Foundation for this problem
- **[Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)** - Similar DFS pattern
- **[Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/)** - Path finding in trees

### Advanced Variants:
- **[Tree Diameter](https://cses.fi/problemset/task/1131/)** - Similar problem for general trees
- **[Diameter of N-Ary Tree](https://leetcode.com/problems/diameter-of-n-ary-tree/)** - Extension to n-ary trees

---

## 📖 Additional Resources

- **LeetCode Problem**: [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)
- **Time Complexity**: O(n)
- **Space Complexity**: O(h)
- **Difficulty**: Easy
- **Category**: Tree, DFS, Binary Tree

### Helpful Concepts:
- **Tree Traversals**: Understanding DFS patterns
- **Height Calculation**: Recursive tree height computation
- **Global State Management**: Using class variables in tree problems

---

## 🎓 Learning Path

### Prerequisites:
1. **Binary Tree Basics** - Structure and traversals
2. **Recursion** - Understanding recursive thinking
3. **DFS** - Depth-first search patterns

### Next Steps:
1. **Binary Tree Maximum Path Sum** - Harder version
2. **Diameter of N-Ary Tree** - Generalization
3. **Tree DP Problems** - Advanced tree algorithms

---

*This problem is an excellent introduction to tree algorithms and demonstrates the power of computing multiple values in a single recursive pass.*
