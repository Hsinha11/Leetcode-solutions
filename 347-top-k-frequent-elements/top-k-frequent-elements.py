class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        heap = []
        for i in d:
            heapq.heappush(heap,(d[i],i))
        return [x[1] for x in heapq.nlargest(k,heap)]