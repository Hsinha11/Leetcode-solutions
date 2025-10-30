class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        idx = haystack.find(needle)
        return idx if idx != -1 else -1
