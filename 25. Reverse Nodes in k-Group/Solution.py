# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """Reverse Nodes in k-Group (LeetCode 25)

    Approach:
        - Use two helpers: (a) find_kth to return the k-th node from a start, or None
          if fewer than k nodes remain; (b) reverse_segment to reverse [head..tail]
          inclusive and return (new_head, new_tail).
        - Iterate the list in segments of length k: if a full segment exists, detach,
          reverse, and stitch back; otherwise connect the remainder as-is.

    Complexity:
        Time:  O(n)
        Space: O(1)
    """

    def reverseKGroup(self, head: 'ListNode', k: int) -> 'ListNode':
        if k <= 1 or head is None:
            return head

        dummy = ListNode(0, head)
        prev_tail = dummy
        ptr = head

        while ptr:
            kth = self._find_kth(ptr, k)
            if kth is None:
                prev_tail.next = ptr
                break

            nxt = kth.next
            kth.next = None
            new_head, new_tail = self._reverse(ptr)
            prev_tail.next = new_head
            new_tail.next = nxt

            prev_tail = new_tail
            ptr = nxt

        return dummy.next

    def _find_kth(self, node: 'ListNode', k: int) -> 'ListNode | None':
        for _ in range(1, k):
            node = node.next
            if node is None:
                return None
        return node

    def _reverse(self, head: 'ListNode') -> tuple['ListNode', 'ListNode']:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev, head

