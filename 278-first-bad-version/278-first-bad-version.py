"""
LeetCode Problem: 278. First Bad Version
Difficulty: Easy

Approach:
Use binary search to minimize API calls.
We check the middle version; if it's bad, the first bad version is to the left,
otherwise it's to the right.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid  # First bad is at mid or before
            else:
                left = mid + 1  # First bad is after mid
        return left
