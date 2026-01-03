class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        l = []
        d = Counter(nums)
        maxi = max(d.values())
        # print(maxi)
        for _ in range(maxi):
            ans = []
            for i in d:
                if d[i]>0:
                    ans.append(i)
                    d[i]-=1
            l.append(ans)

        return l



            

                
