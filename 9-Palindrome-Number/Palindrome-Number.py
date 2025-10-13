class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        x_str = str(x)
        return x_str == x_str[::-1]   

solution = Solution()
print(solution.isPalindrome(121))   # Output: True
print(solution.isPalindrome(-121))  # Output: False
print(solution.isPalindrome(10))    # Output: False
     