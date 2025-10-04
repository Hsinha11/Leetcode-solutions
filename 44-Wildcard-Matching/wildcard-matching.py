from typing import List


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Greedy backtracking for wildcard matching with '?' and '*'.

        - '?' matches any single character.
        - '*' matches any sequence (including empty).

        Approach:
        Two-pointer scan on s and p with backtracking to the last '*':
        - Advance both when characters match or pattern has '?'.
        - On '*', record star position and match index, move pattern ahead.
        - On mismatch without new '*', backtrack to last '*' and extend its match by one.
        - After s ends, remaining pattern must be only '*'.

        Time Complexity: O(n + m) average, worst-case O(n * m) due to backtracking.
        Space Complexity: O(1).
        """

        i = 0  # index in s
        j = 0  # index in p
        star = -1  # last position of '*' in p
        match = 0  # index in s matched after last '*'

        while i < len(s):
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1
            elif star != -1:
                j = star + 1
                match += 1
                i = match
            else:
                return False

        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)


