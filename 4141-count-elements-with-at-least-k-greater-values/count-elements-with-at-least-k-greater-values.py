class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        d ={}
        for i in range(len(nums)):
            d[nums[i]] = i
        c = 0
        for i in range(len(nums)):
            if (len(nums) - d[nums[i]])>k:
                c+=1
        return c
