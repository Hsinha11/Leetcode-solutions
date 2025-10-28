"""
LeetCode Problem 26: Remove Duplicates from Sorted Array

Problem: Given a sorted array nums, remove duplicates in-place such that each 
         element appears only once and return the new length.

Approach: Two Pointers Technique
- Use pointer 'k' to track position for next unique element
- Iterate through array comparing consecutive elements
- When a new unique element is found, place it at position 'k'

Time Complexity: O(n) - single pass through the array
Space Complexity: O(1) - constant extra space, in-place modification
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates from sorted array in-place.
        
        Args:
            nums: A sorted list of integers in non-decreasing order
            
        Returns:
            k: The number of unique elements in the array
            
        Example:
            >>> solution = Solution()
            >>> nums = [1, 1, 2]
            >>> solution.removeDuplicates(nums)
            2
            >>> nums[:2]
            [1, 2]
        """
        # Edge case: empty array
        if not nums:
            return 0
        
        # Initialize pointer for unique elements position
        # k represents the index where the next unique element should be placed
        k = 1  # Start from 1 since first element is always unique
        
        # Iterate through array starting from second element
        for i in range(1, len(nums)):
            # If current element is different from previous element
            # it's a new unique element
            if nums[i] != nums[i - 1]:
                # Place the unique element at position k
                nums[k] = nums[i]
                # Move k pointer forward for next unique element
                k += 1
        
        # Return count of unique elements
        # The first k elements of nums now contain all unique elements
        return k


# Alternative Solution: More explicit with comments for learning
class SolutionAlternative:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Alternative implementation with more explicit logic.
        Same time and space complexity.
        """
        if len(nums) == 0:
            return 0
        
        # Pointer for the position of unique elements
        write_index = 0
        
        for read_index in range(len(nums)):
            # First element OR found a new unique element
            if read_index == 0 or nums[read_index] != nums[read_index - 1]:
                nums[write_index] = nums[read_index]
                write_index += 1
        
        return write_index


# Test cases to verify the solution
def test_solution():
    """Test cases for the removeDuplicates function."""
    solution = Solution()
    
    # Test case 1: Example from problem
    nums1 = [1, 1, 2]
    k1 = solution.removeDuplicates(nums1)
    assert k1 == 2, f"Expected 2, got {k1}"
    assert nums1[:k1] == [1, 2], f"Expected [1, 2], got {nums1[:k1]}"
    print(f"✓ Test 1 passed: nums = [1,1,2] -> {k1}, nums[:k1] = {nums1[:k1]}")
    
    # Test case 2: Example from problem
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = solution.removeDuplicates(nums2)
    assert k2 == 5, f"Expected 5, got {k2}"
    assert nums2[:k2] == [0, 1, 2, 3, 4], f"Expected [0,1,2,3,4], got {nums2[:k2]}"
    print(f"✓ Test 2 passed: nums = [0,0,1,1,1,2,2,3,3,4] -> {k2}, nums[:k2] = {nums2[:k2]}")
    
    # Test case 3: All duplicates
    nums3 = [1, 1, 1, 1]
    k3 = solution.removeDuplicates(nums3)
    assert k3 == 1, f"Expected 1, got {k3}"
    assert nums3[:k3] == [1], f"Expected [1], got {nums3[:k3]}"
    print(f"✓ Test 3 passed: nums = [1,1,1,1] -> {k3}, nums[:k3] = {nums3[:k3]}")
    
    # Test case 4: No duplicates
    nums4 = [1, 2, 3, 4, 5]
    k4 = solution.removeDuplicates(nums4)
    assert k4 == 5, f"Expected 5, got {k4}"
    assert nums4[:k4] == [1, 2, 3, 4, 5], f"Expected [1,2,3,4,5], got {nums4[:k4]}"
    print(f"✓ Test 4 passed: nums = [1,2,3,4,5] -> {k4}, nums[:k4] = {nums4[:k4]}")
    
    # Test case 5: Single element
    nums5 = [1]
    k5 = solution.removeDuplicates(nums5)
    assert k5 == 1, f"Expected 1, got {k5}"
    assert nums5[:k5] == [1], f"Expected [1], got {nums5[:k5]}"
    print(f"✓ Test 5 passed: nums = [1] -> {k5}, nums[:k5] = {nums5[:k5]}")
    
    print("\n✅ All tests passed!")


if __name__ == "__main__":
    # Run test cases
    test_solution()
    
    # Interactive example
    print("\n" + "="*50)
    print("Interactive Example:")
    print("="*50)
    
    solution = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(f"Original array: {nums}")
    
    k = solution.removeDuplicates(nums)
    print(f"Number of unique elements: {k}")
    print(f"Modified array (first {k} elements): {nums[:k]}")
    print(f"Full array (remaining elements don't matter): {nums}")
