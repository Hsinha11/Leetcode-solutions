class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        pali = []
        for i in range(1,5001):
            a = bin(i)[2:]
            # print(a)
            if a==a[::-1]:
                pali.append(int(a,2))
        ans = []
        for i in nums:
            idx = bisect_left(pali,i)
            best = float('inf')
            if idx<len(pali):
                best = abs(pali[idx] - i)
            if idx>0:
                best = min(best,abs(pali[idx-1] - i))
            ans.append(best)
        return ans


            
        # print()
