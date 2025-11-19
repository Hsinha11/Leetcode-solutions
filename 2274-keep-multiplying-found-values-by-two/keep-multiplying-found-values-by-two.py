class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in set(nums):
            original*=2
        return original