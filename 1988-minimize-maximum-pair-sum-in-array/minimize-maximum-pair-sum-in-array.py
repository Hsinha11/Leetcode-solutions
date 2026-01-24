class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        m=-1
        for i in range(len(nums)//2):
            s=nums[i]+nums[len(nums)-1-i]
            m=max(s,m)
        return m
        