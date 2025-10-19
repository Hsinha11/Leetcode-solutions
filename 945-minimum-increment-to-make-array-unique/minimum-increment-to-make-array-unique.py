# Problem: 945. Minimum Increment to Make Array Unique
# Link: https://leetcode.com/problems/minimum-increment-to-make-array-unique/
# Language: Python
# Approach: Sort + Greedy increment
# Time Complexity: O(n log n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        """
        Make all elements in the array unique by incrementing duplicates.
        
        Strategy:
        1. Sort the array to process elements in ascending order
        2. For each element, if it's <= previous element, increment it to prev + 1
        3. Track the total number of increments needed
        
        Args:
            nums: List of integers
            
        Returns:
            Minimum number of moves to make all elements unique
        """
        nums.sort()
        moves = 0
        prev = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] <= prev:
                # Need to increment this element to be unique
                prev += 1
                moves += prev - nums[i]
            else:
                # Element is already unique
                prev = nums[i]
                
        return moves


# Example Usage
if __name__ == "__main__":
    s = Solution()
    
    # Test case 1
    print(s.minIncrementForUnique([3,2,1,2,1,7]))  # Expected output: 6
    
    # Test case 2
    print(s.minIncrementForUnique([1,2,2]))        # Expected output: 1
