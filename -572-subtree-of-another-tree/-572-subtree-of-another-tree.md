# 572. Subtree of Another Tree

> **Difficulty**: Easy  
> **Topics**: Tree, Depth-First Search, String Matching, Binary Tree, Hash Function  
> **Time Complexity**: O(m × n)  
> **Space Complexity**: O(max(m, n)) where m, n are the number of nodes

## 📋 Problem Statement

Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of `subRoot` and `false` otherwise.

A **subtree** of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

### Examples

#### Example 1:
```
root:       subRoot:
    3           4
   / \         / \
  4   5       1   2
 / \
1   2

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Explanation: The subtree rooted at node 4 matches subRoot exactly.
```

#### Example 2:
```
root:       subRoot:
    3           4
   / \         / \
  4   5       1   2
 / \
1   2
   /
  0

Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
Explanation: The subtree rooted at node 4 has an extra node 0.
```

### Constraints:
- The number of nodes in the `root` tree is in the range `[1, 2000]`
- The number of nodes in the `subRoot` tree is in the range `[1, 1000]`
- `-10^4 <= root.val <= 10^4`
- `-10^4 <= subRoot.val <= 10^4`

---

## 🧠 Algorithm Explanation

### Core Concept: Tree Traversal + Tree Comparison

The solution uses two main components:

1. **Tree Traversal**: Visit every node in the main tree as a potential subtree root
2. **Tree Comparison**: For each potential root, check if the subtree matches exactly

### Visual Representation

```
Main Tree:        Check Points:
     3            ✓ Check if subtree starting at 3 matches subRoot
   /   \          ✓ Check if subtree starting at 4 matches subRoot  ← Match!
  4     5         ✓ Check if subtree starting at 5 matches subRoot
 / \              ✓ Check if subtree starting at 1 matches subRoot
1   2             ✓ Check if subtree starting at 2 matches subRoot

SubRoot:
  4
 / \
1   2
```

### Algorithm Steps

1. **Base Cases**: Handle null trees appropriately
2. **Identity Check**: Compare current node's subtree with subRoot
3. **Recursive Search**: If not identical, search in left and right subtrees
4. **Tree Comparison Helper**: Compare two trees for exact structural match

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
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # Helper function to check if two trees are identical
        def isSameTree(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            return (s.val == t.val and
                    isSameTree(s.left, t.left) and
                    isSameTree(s.right, t.right))
        
        # Main logic: check if subRoot is a subtree starting from any node in root
        if not root:
            return False
        if isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


# -------- Example Usage --------
# Example 1:
# root = [3,4,5,1,2], subRoot = [4,1,2]
#       3
#      / \
#     4   5
#    / \
#   1   2

root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

sol = Solution()
print("Is Subtree:", sol.isSubtree(root, subRoot))  # Output: True
```

### C++ Solution

```cpp
#include <iostream>
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
    // Helper function to check if two trees are identical
    bool isSameTree(TreeNode* s, TreeNode* t) {
        if (!s && !t) return true;
        if (!s || !t) return false;
        return (s->val == t->val && 
                isSameTree(s->left, t->left) && 
                isSameTree(s->right, t->right));
    }
    
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (!root) return false;
        if (isSameTree(root, subRoot)) return true;
        return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }
};

// Example usage
int main() {
    // Building main tree: [3,4,5,1,2]
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(4);
    root->right = new TreeNode(5);
    root->left->left = new TreeNode(1);
    root->left->right = new TreeNode(2);
    
    // Building subtree: [4,1,2]
    TreeNode* subRoot = new TreeNode(4);
    subRoot->left = new TreeNode(1);
    subRoot->right = new TreeNode(2);
    
    Solution sol;
    cout << "Is Subtree: " << (sol.isSubtree(root, subRoot) ? "true" : "false") << endl;
    
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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (root == null) return false;
        if (isSameTree(root, subRoot)) return true;
        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    }
    
    private boolean isSameTree(TreeNode s, TreeNode t) {
        if (s == null && t == null) return true;
        if (s == null || t == null) return false;
        return s.val == t.val && 
               isSameTree(s.left, t.left) && 
               isSameTree(s.right, t.right);
    }
}
```

---

## 🔍 Step-by-Step Walkthrough

### Example: root = [3,4,5,1,2], subRoot = [4,1,2]

```
Main Tree:    SubRoot:
    3            4
   / \          / \
  4   5        1   2
 / \
1   2
```

| Step | Current Node | Action | isSameTree Result | Continue Search? |
|------|--------------|--------|-------------------|------------------|
| 1 | 3 | Compare tree at 3 with subRoot | False (3 ≠ 4) | Yes |
| 2 | 4 | Compare tree at 4 with subRoot | **True** ✅ | No - Found! |

**Detailed isSameTree for step 2:**
- Compare root: 4 == 4 ✓
- Compare left: isSameTree(1, 1) ✓
- Compare right: isSameTree(2, 2) ✓
- **Result**: True

---

## 🎯 Key Insights

### 1. **Two-Function Approach**
```python
# Main function: Find potential subtree roots
def isSubtree(root, subRoot):
    # Check current node + recurse to children
    
# Helper function: Compare two complete trees
def isSameTree(s, t):
    # Structural and value comparison
```

### 2. **Base Case Handling**
```python
# Both null: trees match
if not s and not t: return True

# One null, one not: trees don't match  
if not s or not t: return False

# Both exist: compare values and recurse
return s.val == t.val and ...
```

### 3. **Short-Circuit Evaluation**
```python
# Use OR to stop as soon as match is found
return (self.isSubtree(root.left, subRoot) or 
        self.isSubtree(root.right, subRoot))
```

### 4. **Recursive Pattern**
- **isSubtree**: Searches for starting point
- **isSameTree**: Validates exact match from starting point

---

## 📊 Complexity Analysis

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| **DFS + Tree Comparison** | **O(m × n)** | **O(max(m, n))** | Standard solution |
| String Serialization | O(m + n) | O(m + n) | Advanced optimization |
| Hash-based | O(m + n) | O(m + n) | Rolling hash approach |

**Where:**
- `m` = number of nodes in main tree
- `n` = number of nodes in subtree

### Worst Case Analysis:
```
Main Tree:     SubRoot:
   1              1
  /              /
 1              1  
/              /
1             1
...           ...
```
**Time**: O(m × n) - check every node, compare full subtree each time

---

## 🧪 Test Cases

### Basic Cases
```python
# Test 1: Exact subtree match
root = [3,4,5,1,2]
subRoot = [4,1,2]
# Expected: True

# Test 2: No match due to extra node
root = [3,4,5,1,2,null,null,null,null,0]
subRoot = [4,1,2]
# Expected: False
```

### Edge Cases
```python
# Test 3: Single node trees
root = [1]
subRoot = [1]
# Expected: True

# Test 4: SubRoot larger than root
root = [1]
subRoot = [1,2]
# Expected: False

# Test 5: Empty subtree (invalid input, but conceptually)
root = [1,2,3]
subRoot = []
# Expected: False (by definition)
```

### Advanced Cases
```python
# Test 6: Multiple potential matches
root = [4,1,2,4,1,2]
subRoot = [4,1,2]
# Expected: True (multiple valid subtrees)

# Test 7: Similar structure, different values
root = [1,2,3]
subRoot = [1,2,4]
# Expected: False

# Test 8: Subtree is the entire tree
root = [1,2,3]
subRoot = [1,2,3]
# Expected: True
```

---

## 🚀 Alternative Approaches

### 1. **String Serialization Approach** (O(m + n))

```python
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def serialize(node):
            if not node:
                return "#"
            return f"^{node.val},{serialize(node.left)},{serialize(node.right)}$"
        
        root_str = serialize(root)
        sub_str = serialize(subRoot)
        
        return sub_str in root_str

# Example serialization:
# Tree [4,1,2] becomes "^4,^1,#,#,^2,#,#$"
# Use special markers (^,$) to avoid false matches
```

### 2. **Hash-Based Approach** (Rolling Hash)

```python
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def get_hash(node, memo):
            if not node:
                return 0
            
            if node in memo:
                return memo[node]
            
            left_hash = get_hash(node.left, memo)
            right_hash = get_hash(node.right, memo)
            
            # Rolling hash function
            current_hash = hash((node.val, left_hash, right_hash))
            memo[node] = current_hash
            return current_hash
        
        target_hash = get_hash(subRoot, {})
        
        def dfs(node):
            if not node:
                return False
            if get_hash(node, {}) == target_hash and self.isSameTree(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)
```

### 3. **Merkle Tree Approach** (Cryptographic Hash)

```python
import hashlib

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def merkle_hash(node):
            if not node:
                return hashlib.sha256(b"null").hexdigest()
            
            left_hash = merkle_hash(node.left)
            right_hash = merkle_hash(node.right)
            
            combined = f"{node.val}#{left_hash}#{right_hash}"
            return hashlib.sha256(combined.encode()).hexdigest()
        
        target_hash = merkle_hash(subRoot)
        
        def dfs(node):
            if not node:
                return False
            if merkle_hash(node) == target_hash:
                return True
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)
```

---

## 📈 Performance Comparison

### Approach Analysis

| Method | Best Case | Average Case | Worst Case | Space | Pros | Cons |
|--------|-----------|--------------|------------|-------|------|------|
| **DFS + Compare** | O(n) | O(m×n) | O(m×n) | O(h) | Simple, reliable | Can be slow |
| **Serialization** | O(m+n) | O(m+n) | O(m+n) | O(m+n) | Fast, elegant | Memory intensive |
| **Rolling Hash** | O(m+n) | O(m+n) | O(m+n)* | O(m+n) | Very fast | Hash collisions |

*Hash collisions might require fallback to tree comparison

---

## 💡 Tips for Interview

### Key Points to Mention:
1. **Problem understanding**: Subtree must be exact structural match
2. **Two-step approach**: Find candidates + verify match
3. **Base case handling**: Null tree comparisons
4. **Optimization opportunities**: Serialization for better time complexity

### Common Mistakes:
- Confusing subtree with subset (structure must match exactly)
- Incorrect null handling in tree comparison
- Forgetting to check all possible subtree roots
- Not considering edge case where subtree equals entire tree

### Follow-up Questions:
- How to optimize for better time complexity? (Serialization)
- What if we need to find all subtree occurrences?
- How to handle very large trees? (Iterative approaches)
- What about trees with duplicate values? (Current solution handles this)

---

## 🔧 Optimizations

### 1. **Early Termination**
```python
def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
    # Early termination: if main tree smaller than subtree
    def count_nodes(node):
        return 0 if not node else 1 + count_nodes(node.left) + count_nodes(node.right)
    
    if count_nodes(root) < count_nodes(subRoot):
        return False
    
    # Continue with normal algorithm...
```

### 2. **Memoization for Repeated Subtrees**
```python
def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
    memo = {}
    
    def isSameTree(s, t):
        if (s, t) in memo:
            return memo[(s, t)]
        
        if not s and not t:
            result = True
        elif not s or not t:
            result = False
        else:
            result = (s.val == t.val and 
                     isSameTree(s.left, t.left) and 
                     isSameTree(s.right, t.right))
        
        memo[(s, t)] = result
        return result
    
    # Rest of implementation...
```

### 3. **Iterative Implementation** (Stack Overflow Prevention)
```python
def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
    if not root:
        return False
    
    stack = [root]
    
    while stack:
        node = stack.pop()
        if self.isSameTree(node, subRoot):
            return True
        
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    return False
```

---

## 📚 Related Problems

### Direct Extensions:
- **[Same Tree](https://leetcode.com/problems/same-tree/)** - Core helper function
- **[Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)** - Tree structure comparison
- **[Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)** - Tree manipulation

### Advanced Variants:
- **[Subtree of Another Tree with Operations](https://leetcode.com/problems/flip-equivalent-binary-trees/)** - Allow transformations
- **[Binary Tree Cameras](https://leetcode.com/problems/binary-tree-cameras/)** - Complex tree DP
- **[All Nodes Distance K](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)** - Tree relationships

### String Matching Connection:
- **[Find All Anagrams](https://leetcode.com/problems/find-all-anagrams-in-a-string/)** - Pattern matching
- **[KMP Algorithm](https://leetcode.com/problems/repeated-substring-pattern/)** - Efficient string search

---

## 📖 Additional Resources

- **LeetCode Problem**: [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)
- **Time Complexity**: O(m × n)
- **Space Complexity**: O(max(m, n))
- **Difficulty**: Easy
- **Category**: Tree, DFS, String Matching

### Helpful Concepts:
- **Tree Traversal**: DFS pattern for tree exploration
- **Tree Comparison**: Structural equality checking
- **String Algorithms**: Serialization and pattern matching
- **Hash Functions**: For optimization approaches

---

## 🎓 Learning Path

### Prerequisites:
1. **Binary Tree Traversal** - DFS understanding
2. **Tree Comparison** - Same Tree problem
3. **Recursion** - Nested recursive calls
4. **String Matching** - For advanced approaches

### Skill Building:
1. **Start**: Same Tree (leetcode.com/problems/same-tree/)
2. **Practice**: This problem with basic approach
3. **Optimize**: Implement serialization method
4. **Advanced**: Hash-based approaches

### Next Steps:
1. **Harder Tree Problems** - Path sum, diameter
2. **String Pattern Matching** - KMP, Rabin-Karp
3. **Advanced Tree DP** - More complex tree algorithms

---

*This problem beautifully combines tree traversal with structural comparison, serving as an excellent introduction to more complex tree algorithms and optimization techniques.*
