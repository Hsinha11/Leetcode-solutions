class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        ans=[]
        heap = []
        for i in d:
            heapq.heappush(heap,(d[i],i))
            while len(heap)>k:
                heapq.heappop(heap)
        for i in heap:
            ans.extend([i[1]]*i[0])
        final_result = sorted(ans, key=lambda x: (-d[x], -x))
        return final_result
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans=[]
        for i in range(k,len(nums)+1):
            # print(self.topKFrequent(nums[:i],x))    
            ans.append(sum(self.topKFrequent(nums[i-k:i],x)))
        return ans