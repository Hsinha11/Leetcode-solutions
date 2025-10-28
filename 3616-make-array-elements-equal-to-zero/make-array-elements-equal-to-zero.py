class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        c=0
        n = len(nums)
        left=[0]*n
        right = [0]*n
        left[0] = nums[0]
        right[-1] = nums[-1]
        for i in range(1,n):
            left[i] = left[i-1]+nums[i]
        for i in range(n-2,-1,-1):
            right[i] = right[i+1]+ nums[i]
        for i in range(n):
            if nums[i]==0:
                if left[i]==right[i]:
                    c+=2
                if right[i]-1 ==left[i]:
                    c+=1
                if left[i]-1 ==right[i]:
                    c+=1
        return c