class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        d ={ }
        # for i in range(len(nums)):
        #    rev = int(str(nums[i])[::-1])
        #    d[rev] = i
        # print(d)
        d[int(str(nums[0])[::-1])] = 0 
        ans = 10**18
        for i in range(1,len(nums)):
            if nums[i] in d :
                # print(i, d[nums[i]])
                ans = min(ans,(i - d[nums[i]]))
            d[int(str(nums[i])[::-1])] = i
        if ans==10**18:
            return -1
        return ans
        