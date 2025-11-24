import sys
sys.setrecursionlimit(100000)
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = {}
        def f(index,curr):
            if index==len(nums):
                if curr==0:
                    return 0
                else:
                    return float('-inf')
            if (index,curr) in dp:
                return dp[(index,curr)]

            notp = f(index+1,curr)
            newrem = (curr+nums[index])%3
            pick = nums[index]+ f(index+1,newrem)
            ans = max(pick,notp)
            dp[(index,curr)] = ans
            return max(pick,notp)
        ans = f(0,0)
        return ans