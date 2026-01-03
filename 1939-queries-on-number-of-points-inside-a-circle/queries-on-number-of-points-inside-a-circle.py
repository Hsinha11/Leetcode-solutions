class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(queries)
        ans = [0]*n
        for i in range(n):
            h,k,r = queries[i]
            for x,y in points:
                if (x-h)**2 + (y-k)**2 <=r**2:
                    ans[i]+=1
        return ans