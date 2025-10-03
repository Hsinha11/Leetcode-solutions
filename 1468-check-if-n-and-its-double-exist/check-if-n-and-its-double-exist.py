from typing import List


class Solution:
    """Check If N and Its Double Exist (LeetCode 1346)

    Approach:
        Iterate through the array while maintaining a set of previously seen values.
        For each value x, if 2*x is in the set, then some earlier number is double x.
        Also, if x is even and x//2 is in the set, then some earlier number is half of x.
        If either condition holds, return True. Otherwise add x to the set and continue.

    Complexity:
        Time:  O(n) — each element is processed once with O(1) average lookups.
        Space: O(n) — to store up to n seen elements in the set.
    """

    def checkIfExist(self, arr: List[int]) -> bool:
        seen: set[int] = set()
        for value in arr:
            if (value * 2) in seen or (value % 2 == 0 and (value // 2) in seen):
                return True
            seen.add(value)
        return False

