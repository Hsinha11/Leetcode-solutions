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
