class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        freq = [0]*(n+1)
        ans = []
        for i in range(n):
            freq[A[i]]+=1
            freq[B[i]]+=1
            c = 0
            ans.append(freq.count(2))
        return ans