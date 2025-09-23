class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:

        heapq.heappush(self.max_heap, -num)
        val = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
        
    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap) :
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0])/2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()