from typing import Optional, List


class Codec:
    """
    Serialize and deserialize a Binary Search Tree (BST).

    Approach:
    - Serialize using preorder traversal (root-left-right). We output values joined by spaces.
    - Deserialize by consuming the preorder sequence with lower/upper bounds to reconstruct the BST in O(n):
      each value belongs to exactly one subtree defined by bounds (min_val, max_val).

    Time Complexity: O(n) for both serialize and deserialize, where n is number of nodes.
    Space Complexity: O(n) for output and recursion stack in worst case (skewed tree).
    """

    def serialize(self, root: Optional[TreeNode]) -> str:
        values: List[str] = []

        def preorder(node: Optional[TreeNode]) -> None:
            if not node:
                return
            values.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return " ".join(values)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        preorder_values: List[int] = list(map(int, data.split()))
        index: List[int] = [0]  # mutable index captured by closure

        def build(min_val: int, max_val: int) -> Optional[TreeNode]:
            if index[0] == len(preorder_values):
                return None
            val = preorder_values[index[0]]
            # Enforce strict BST bounds: min_val < val < max_val
            if not (min_val < val < max_val):
                return None
            index[0] += 1
            node = TreeNode(val)
            node.left = build(min_val, val)
            node.right = build(val, max_val)
            return node

        return build(float('-inf'), float('inf'))


# The Codec class will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


