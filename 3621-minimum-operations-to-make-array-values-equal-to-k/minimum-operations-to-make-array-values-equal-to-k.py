class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if k>min(nums):
            return -1
        s=set()
        for i in nums:
            if i>k:
                s.add(i)
        return len(s) 