class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        l= sorted(zip(capital,profits))
        maxi = w
        heap = []
        i=0
        for _ in range(k):
            while i< len(l) and l[i][0]<=maxi:
                heapq.heappush(heap,-l[i][1])
                i+=1
            if heap:
                maxi+=-heapq.heappop(heap)
        return maxi