class Solution:
    def countPartitions(self, l: List[int]) -> int:
        if sum(l)%2==0:
            return len(l)-1
        return 0