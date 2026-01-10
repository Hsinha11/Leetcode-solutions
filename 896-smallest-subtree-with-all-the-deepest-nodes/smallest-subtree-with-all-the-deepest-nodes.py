# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def depth(root):
            if not root:return 0
            left  = depth(root.left)
            right = depth(root.right)
            return 1 + max(left,right)
        height = depth(root)
        def f(root,h):
            if not root:
                return None
            if height-1 == h:
                return root
            left = f(root.left,h+1)
            right = f(root.right,h+1)
            if left and right:return root
            return left if left else right
        node = f(root,0)
        return node