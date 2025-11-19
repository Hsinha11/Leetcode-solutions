class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l=[x for x in range(1,10001) if x not in arr]
        return l[k-1]
        