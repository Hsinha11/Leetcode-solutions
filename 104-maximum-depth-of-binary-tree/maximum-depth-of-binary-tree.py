# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
d = {}
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root in d:
            return d[root]
        left =1+ self.maxDepth(root.left)
        right = 1 + self.maxDepth(root.right)
        d[root] = max(left,right)
        return d[root]