"""
LeetCode 1903: Largest Odd Number in String

Problem:
You are given a string num representing a large integer. Return the largest-valued 
odd integer (as a string) that is a substring of num, or an empty string "" if no 
odd integer exists.

A substring is a contiguous sequence of characters within a string.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def largestOddNumber(self, num):
        """
        Find the largest odd number that is a substring of the given string.
        
        Args:
            num: String representing a large integer
            
        Returns:
            str: The largest odd number as a string, or empty string if none exists
        """
        # Iterate from right to left to find the rightmost odd digit
        for i in range(len(num) - 1, -1, -1):
            # Check if current digit is odd
            if int(num[i]) % 2 == 1:
                # Return substring from start to current position (inclusive)
                return num[:i + 1]
        
        # If no odd digit found, return empty string
        return ""


# Alternative implementation using a more Pythonic approach
class SolutionAlternative:
    def largestOddNumber(self, num):
        """
        Alternative implementation using enumerate and next() function.
        """
        # Find the rightmost odd digit
        for i, digit in enumerate(reversed(num)):
            if int(digit) % 2 == 1:
                # Return substring from start to the position of this odd digit
                return num[:len(num) - i]
        
        return ""


# Test cases
def test_solution():
    """Test the solution with provided examples."""
    solution = Solution()
    
    # Example 1: num = "52"
    # Expected output: "5"
    result1 = solution.largestOddNumber("52")
    print(f"Example 1: '52' -> '{result1}'")  # Should output "5"
    
    # Example 2: num = "4206"
    # Expected output: ""
    result2 = solution.largestOddNumber("4206")
    print(f"Example 2: '4206' -> '{result2}'")  # Should output ""
    
    # Example 3: num = "35427"
    # Expected output: "35427"
    result3 = solution.largestOddNumber("35427")
    print(f"Example 3: '35427' -> '{result3}'")  # Should output "35427"
    
    # Additional test cases
    test_cases = [
        ("123456", "12345"),  # Rightmost odd is 5
        ("2468", ""),         # No odd digits
        ("13579", "13579"),   # All odd digits
        ("1000", "1"),        # Only first digit is odd
        ("2001", "2001"),     # Only last digit is odd
    ]
    
    print("\nAdditional test cases:")
    for input_str, expected in test_cases:
        result = solution.largestOddNumber(input_str)
        status = "✅" if result == expected else "❌"
        print(f"{status} '{input_str}' -> '{result}' (expected: '{expected}')")


if __name__ == "__main__":
    test_solution()
