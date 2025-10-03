import bisect
from typing import List


class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        # Step 1: Sort the list of flowers to process gardens in ascending order
        flowers.sort()
        n = len(flowers)
        
        # Step 2: Find the first garden that already has at least 'target' flowers using binary search
        m = bisect.bisect_left(flowers, target)
        
        # Initial beauty from gardens that are already full
        init_beauty = (n - m) * full
        
        # If all gardens are already complete, return the initial beauty
        if m == 0:
            return init_beauty

        # Step 3: Precompute the number of flowers needed to fill each garden to its target
        # 'need[i]' stores the number of flowers needed to complete the i-th incomplete garden
        flowers_needed = [0] * m
        for i in range(1, m):
            flowers_needed[i] = flowers_needed[i - 1] + (flowers[i] - flowers[i - 1]) * i

        # Step 4: Calculate the maximum beauty by filling some incomplete gardens to the target
        max_beauty = self.calculate_partial_garden_beauty(flowers_needed, newFlowers, flowers, target, partial, m)

        # Step 5: Try to make gardens complete by using available newFlowers
        for i in range(m - 1, -1, -1):
            if flowers[i] + newFlowers < target:
                break  # No point in continuing if the current garden cannot be filled to the target
            
            # Spend flowers to fill the current garden to its target
            newFlowers -= (target - flowers[i])
            
            # Calculate partial beauty with remaining newFlowers after making this garden full
            partial_beauty = self.calculate_partial_garden_beauty(flowers_needed, newFlowers, flowers, target, partial, i)
            
            # Update the maximum beauty
            max_beauty = max(max_beauty, partial_beauty + full * (m - i))

        # Return the final beauty, including the initial beauty from complete gardens
        return max_beauty + init_beauty

    def calculate_partial_garden_beauty(self, flowers_needed, newFlowers, flowers, target, partial, ind):
        # If there are no incomplete gardens, return 0 beauty for partial gardens
        if ind == 0:
            return 0
        
        # Step 6: Perform binary search to find the maximum number of flowers we can add
        # to the incomplete gardens without exceeding the available 'newFlowers'
        index = bisect.bisect_right(flowers_needed, newFlowers)
        
        # Ensure we do not exceed the number of incomplete gardens
        index = min(index, ind)
        
        # Calculate the maximum number of flowers that can be added without exceeding target-1
        max_possible = flowers[index - 1] + (newFlowers - flowers_needed[index - 1]) // index
        max_possible = min(max_possible, target - 1)  # No garden can have more than target-1 flowers
        
        # Return the beauty of the incomplete gardens based on the minimum value of the gardens
        return max_possible * partial