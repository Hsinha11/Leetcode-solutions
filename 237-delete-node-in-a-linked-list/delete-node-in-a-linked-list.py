# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """Delete Node in a Linked List (LeetCode 237)

    Approach:
        We are given only the node to delete, not the head. Copy the value from
        the next node into the current node, then bypass the next node by
        setting current.next = current.next.next. This effectively removes the
        next node, achieving the required deletion semantics.

    Complexity:
        Time:  O(1)
        Space: O(1)
    """

    def deleteNode(self, node: 'ListNode') -> None:
        node.val = node.next.val
        node.next = node.next.next

