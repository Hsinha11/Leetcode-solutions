class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans =target[0]
        for i in range(1,len(target)):
            ans+=max(target[i]-target[i-1],0)
        return ans
