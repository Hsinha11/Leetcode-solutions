class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        d=defaultdict(int)
        for i,c in zip(s,cost):
            d[i]+=c
        return sum(d.values()) - max(d.values())
        
        
        