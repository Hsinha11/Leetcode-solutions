from typing import List
import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10**9 + 7

        # Pair up (efficiency, speed) and sort by efficiency descending
        engineers = sorted(zip(efficiency, speed), key=lambda x: -x[0])

        speed_heap = []         # min-heap to keep top k speeds
        sum_speed = 0           # sum of speeds in the heap
        best = 0

        for eff, sp in engineers:
            # add current engineer's speed
            heapq.heappush(speed_heap, sp)
            sum_speed += sp

            # if we exceed k members, remove the smallest speed
            if len(speed_heap) > k:
                sum_speed -= heapq.heappop(speed_heap)

            # current performance with current efficiency as minimum
            best = max(best, sum_speed * eff)

        return best % MOD


# quick example usage
if __name__ == "__main__":
    sol = Solution()
    n = 6
    speed = [2,10,3,1,5,8]
    efficiency = [5,4,3,9,7,2]
    k = 3
    print(sol.maxPerformance(n, speed, efficiency, k))  # expected 68