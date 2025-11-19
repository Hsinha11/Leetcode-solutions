class Solution:
    def halveArray(self, nums: List[int]) -> int:
        # heap =[]
        c=0
        s = sum(nums)
        curr= 0 
        heap = [-x for x in nums]
        heapify(heap)
        while curr<s/2:
            half = heap[0]/2
            curr+=-half
            c+=1
            heapreplace(heap,half)
            # heapq.heapify(heap)
        return c