"""
LeetCode 2965: Find Missing and Repeated Values

Problem:
You are given a 0-indexed 2D integer matrix grid of size n x n with values in the range [1, n²]. 
Each integer appears exactly once except:
- One number a appears twice
- One number b is missing

Your task is to find the repeated and missing numbers.

Time Complexity: O(n²)
Space Complexity: O(n²)
"""

class Solution:
    def findMissingAndRepeatedValues(self, grid):
        """
        Find the repeated and missing values in a 2D grid.
        
        Args:
            grid: 2D integer matrix of size n x n with values in range [1, n²]
            
        Returns:
            List[int]: [repeated_value, missing_value]
        """
        n = len(grid)
        size = n * n
        count = [0] * (size + 1)  # Count array for numbers 1 to n²
        
        # Count occurrences of each number in the grid
        for i in range(n):
            for j in range(n):
                count[grid[i][j]] += 1
        
        a = b = -1  # Initialize repeated and missing values
        
        # Find the repeated and missing numbers
        for num in range(1, size + 1):
            if count[num] == 2:
                a = num  # Found the repeated number
            elif count[num] == 0:
                b = num  # Found the missing number
        
        return [a, b]


# Test cases
def test_solution():
    """Test the solution with provided examples."""
    solution = Solution()
    
    # Example 1: grid = [[1,3],[2,2]]
    # Expected output: [2,4]
    grid1 = [[1,3],[2,2]]
    result1 = solution.findMissingAndRepeatedValues(grid1)
    print(f"Example 1: {grid1} -> {result1}")  # Should output [2,4]
    
    # Example 2: grid = [[9,1,7],[8,9,2],[3,4,6]]
    # Expected output: [9,5]
    grid2 = [[9,1,7],[8,9,2],[3,4,6]]
    result2 = solution.findMissingAndRepeatedValues(grid2)
    print(f"Example 2: {grid2} -> {result2}")  # Should output [9,5]


if __name__ == "__main__":
    test_solution()
