# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(l,r):
            if l is None and r is None:return True
            if l is None or r is None:return False
            return l.val==r.val and dfs(l.left,r.right) and dfs(l.right,r.left)
        return dfs(root.left,root.right)