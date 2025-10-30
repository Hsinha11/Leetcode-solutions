"""
LeetCode Problem 283: Move Zeroes

Problem: Given an integer array nums, move all 0's to the end while maintaining 
         the relative order of non-zero elements. Must be done in-place.

Approach: Two Pointers Technique (Optimal)
- Use 'left' pointer to track position for next non-zero element
- Use 'right' pointer to traverse the array
- Swap non-zero elements to the front, zeros naturally move to back

Time Complexity: O(n) - single pass through array
Space Complexity: O(1) - in-place with constant extra space
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Move all zeros to the end while maintaining relative order of non-zeros.
        Modifies array in-place.
        
        Args:
            nums: List of integers to modify in-place
            
        Returns:
            None: Modifies nums in-place
            
        Example:
            >>> solution = Solution()
            >>> nums = [0, 1, 0, 3, 12]
            >>> solution.moveZeroes(nums)
            >>> nums
            [1, 3, 12, 0, 0]
        """
        # Pointer for position of next non-zero element
        left = 0
        
        # Traverse array with right pointer
        for right in range(len(nums)):
            # When we find a non-zero element
            if nums[right] != 0:
                # Swap it with the element at left pointer
                nums[left], nums[right] = nums[right], nums[left]
                # Move left pointer forward
                left += 1
        
        # After loop: all non-zeros are at front, zeros at back


# Alternative Solution: More Explicit Two-Pass Approach
class SolutionTwoPass:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Alternative two-pass approach (less optimal but easier to understand).
        
        Pass 1: Move all non-zero elements to front
        Pass 2: Fill remaining positions with zeros
        """
        # First pass: collect all non-zero elements
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
        
        # Second pass: fill remaining with zeros
        for i in range(left, len(nums)):
            nums[i] = 0


# Alternative Solution: Snowball Approach (Creative)
class SolutionSnowball:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        'Snowball' approach - imagine zeros rolling like a snowball.
        
        Track the size of the 'snowball' (consecutive zeros).
        When we hit a non-zero, swap it with the first zero in the snowball.
        """
        snowball_size = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                # Snowball grows
                snowball_size += 1
            elif snowball_size > 0:
                # Non-zero found, swap with first zero in snowball
                # This effectively 'rolls' the snowball forward
                nums[i], nums[i - snowball_size] = nums[i - snowball_size], nums[i]


def test_solution():
    """Comprehensive test cases for moveZeroes function."""
    
    # Test with optimal solution
    solution = Solution()
    
    # Test case 1: Example from problem
    nums1 = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums1)
    assert nums1 == [1, 3, 12, 0, 0], f"Expected [1,3,12,0,0], got {nums1}"
    print(f"✓ Test 1 passed: [0,1,0,3,12] -> {nums1}")
    
    # Test case 2: Single zero
    nums2 = [0]
    solution.moveZeroes(nums2)
    assert nums2 == [0], f"Expected [0], got {nums2}"
    print(f"✓ Test 2 passed: [0] -> {nums2}")
    
    # Test case 3: No zeros
    nums3 = [1, 2, 3, 4, 5]
    solution.moveZeroes(nums3)
    assert nums3 == [1, 2, 3, 4, 5], f"Expected [1,2,3,4,5], got {nums3}"
    print(f"✓ Test 3 passed: [1,2,3,4,5] -> {nums3}")
    
    # Test case 4: All zeros
    nums4 = [0, 0, 0, 0]
    solution.moveZeroes(nums4)
    assert nums4 == [0, 0, 0, 0], f"Expected [0,0,0,0], got {nums4}"
    print(f"✓ Test 4 passed: [0,0,0,0] -> {nums4}")
    
    # Test case 5: Zeros at beginning
    nums5 = [0, 0, 1, 2, 3]
    solution.moveZeroes(nums5)
    assert nums5 == [1, 2, 3, 0, 0], f"Expected [1,2,3,0,0], got {nums5}"
    print(f"✓ Test 5 passed: [0,0,1,2,3] -> {nums5}")
    
    # Test case 6: Zeros at end (already in position)
    nums6 = [1, 2, 3, 0, 0]
    solution.moveZeroes(nums6)
    assert nums6 == [1, 2, 3, 0, 0], f"Expected [1,2,3,0,0], got {nums6}"
    print(f"✓ Test 6 passed: [1,2,3,0,0] -> {nums6}")
    
    # Test case 7: Alternating zeros and non-zeros
    nums7 = [0, 1, 0, 2, 0, 3]
    solution.moveZeroes(nums7)
    assert nums7 == [1, 2, 3, 0, 0, 0], f"Expected [1,2,3,0,0,0], got {nums7}"
    print(f"✓ Test 7 passed: [0,1,0,2,0,3] -> {nums7}")
    
    # Test case 8: Single non-zero element
    nums8 = [1]
    solution.moveZeroes(nums8)
    assert nums8 == [1], f"Expected [1], got {nums8}"
    print(f"✓ Test 8 passed: [1] -> {nums8}")
    
    # Test case 9: Negative numbers
    nums9 = [0, -1, 0, -3, 12]
    solution.moveZeroes(nums9)
    assert nums9 == [-1, -3, 12, 0, 0], f"Expected [-1,-3,12,0,0], got {nums9}"
    print(f"✓ Test 9 passed: [0,-1,0,-3,12] -> {nums9}")
    
    print("\n✅ All tests passed!")
    
    # Compare with alternative solutions
    print("\n" + "="*50)
    print("Testing Alternative Solutions:")
    print("="*50)
    
    # Test two-pass solution
    solution2 = SolutionTwoPass()
    nums_test = [0, 1, 0, 3, 12]
    solution2.moveZeroes(nums_test)
    assert nums_test == [1, 3, 12, 0, 0]
    print(f"✓ Two-Pass Solution: [0,1,0,3,12] -> {nums_test}")
    
    # Test snowball solution
    solution3 = SolutionSnowball()
    nums_test2 = [0, 1, 0, 3, 12]
    solution3.moveZeroes(nums_test2)
    assert nums_test2 == [1, 3, 12, 0, 0]
    print(f"✓ Snowball Solution: [0,1,0,3,12] -> {nums_test2}")
    
    print("\n✅ All alternative solutions work correctly!")


def demonstrate_step_by_step():
    """Demonstrate the algorithm step by step."""
    print("\n" + "="*50)
    print("Step-by-Step Demonstration:")
    print("="*50)
    
    nums = [0, 1, 0, 3, 12]
    print(f"\nOriginal array: {nums}\n")
    
    left = 0
    for right in range(len(nums)):
        print(f"Step {right + 1}:")
        print(f"  right={right}, left={left}")
        print(f"  nums[{right}] = {nums[right]}", end="")
        
        if nums[right] != 0:
            print(f" (non-zero) -> swap with nums[{left}]")
            nums[left], nums[right] = nums[right], nums[left]
            print(f"  Array after swap: {nums}")
            left += 1
        else:
            print(f" (zero) -> skip")
            print(f"  Array unchanged: {nums}")
        print()
    
    print(f"Final result: {nums}")
    print(f"All non-zeros moved to front, zeros at back! ✓")


if __name__ == "__main__":
    # Run comprehensive tests
    test_solution()
    
    # Show step-by-step demonstration
    demonstrate_step_by_step()
    
    # Interactive example
    print("\n" + "="*50)
    print("Interactive Example:")
    print("="*50)
    
    solution = Solution()
    test_cases = [
        [0, 1, 0, 3, 12],
        [1, 2, 0, 0, 3, 0, 4],
        [0, 0, 0, 1]
    ]
    
    for nums in test_cases:
        original = nums.copy()
        solution.moveZeroes(nums)
        print(f"{original} -> {nums}")
