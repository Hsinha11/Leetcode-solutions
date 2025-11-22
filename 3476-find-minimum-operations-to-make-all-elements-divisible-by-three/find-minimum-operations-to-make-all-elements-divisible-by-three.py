class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(min(nums[i] % 3, 3 - (nums[i] % 3)) for i in range(len(nums)))