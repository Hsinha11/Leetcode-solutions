class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxi =0
        for i in range(len(nums)):
            c=0
            for j in range(len(nums)):
                c|=nums[j]
                maxi = max(c,maxi)
        ans = [0]
        def subset(nums,maxi,i,cor,ans):
            if i==len(nums):
                if cor==maxi:
                    ans[0]+=1
                return
            subset(nums,maxi,i+1,cor|nums[i],ans)
            subset(nums,maxi,i+1,cor,ans)
        subset(nums,maxi,0,0,ans)
        return ans[0]