class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = len(nums)
        l=[False]*n
        k = 0 
        for i in range(n):
            k = ((k<<1) | nums[i] )%5
            l[i]= (k==0)
        return l
            
