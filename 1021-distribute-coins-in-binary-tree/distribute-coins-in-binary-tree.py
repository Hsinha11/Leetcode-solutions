from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = 0

        def postorder(node: Optional[TreeNode]) -> int:
            nonlocal moves
            if not node:
                return 0

            left_balance = postorder(node.left)
            right_balance = postorder(node.right)

            moves += abs(left_balance) + abs(right_balance)

            # Return this node's balance to parent: positive -> surplus coins, negative -> deficit
            return node.val + left_balance + right_balance - 1

        postorder(root)
        return moves

