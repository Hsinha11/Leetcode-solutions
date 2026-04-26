# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        def post(root):
            if not root:return None
            if root.left:post(root.left)
            if root.right:post(root.right)
            l.append(root.val)
        post(root)
        return l