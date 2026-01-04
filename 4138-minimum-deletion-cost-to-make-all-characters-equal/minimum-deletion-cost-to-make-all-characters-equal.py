class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        d={}
        for i in range(len(s)):
            d[s[i]] = d.get(s[i],0)+cost[i]
        # d = dict(sorted(d.items(),key = lambda x: x[1],reverse=True))
        # print(d)
        s = sum(d.values())
        maxi = max(d.values())
        return (s-maxi)
        
        
        