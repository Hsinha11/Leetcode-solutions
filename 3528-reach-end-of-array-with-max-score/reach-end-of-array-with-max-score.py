class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        ind = 0
        ans =0
        for i in range(len(nums)):
            if nums[i]>nums[ind]:
                ans+=(i-ind)*nums[ind]
                ind=i
        # if ans==0:
        ans += (len(nums)-1 - ind)*nums[ind]
        return ans