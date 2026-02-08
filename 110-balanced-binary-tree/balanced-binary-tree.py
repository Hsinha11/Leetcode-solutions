# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self,root):
        if not root:return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        return 1 + max(left,right)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root ==None:return True
        left = self.depth(root.left)
        right = self.depth(root.right)
        if abs(left- right) > 1 : 
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)