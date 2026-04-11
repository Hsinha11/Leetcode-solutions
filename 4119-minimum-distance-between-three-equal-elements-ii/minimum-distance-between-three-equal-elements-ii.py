class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        d= DefaultDict(list)
        for i in range(len(nums)):
            d[nums[i]].append(i)
        ans = 10**9
        for i in d:
            winsize = len(d[i])
            l = d[i]
            if winsize>=3:
                for x in range(winsize-2):
                    ans = min(ans, 2 * (l[x+2] - l[x]))
        if ans==10**9:
            return -1
        else:
            return ans