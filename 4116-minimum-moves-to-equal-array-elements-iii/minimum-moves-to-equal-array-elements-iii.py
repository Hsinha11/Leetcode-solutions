class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(max(nums)-x for x in nums)