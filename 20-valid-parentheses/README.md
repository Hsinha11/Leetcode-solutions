# Valid Parentheses - LeetCode #20

## Problem Statement
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Examples
```
Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Input: s = "([)]"
Output: false

Input: s = "{[]}"
Output: true
```

## Approach
**Key Insight**: Use a stack to keep track of opening brackets and match them with closing brackets.

**Algorithm**:
1. Initialize an empty stack.
2. Iterate through each character in the string.
3. If it's an opening bracket, push it onto the stack.
4. If it's a closing bracket:
   - Check if stack is empty (return false if so)
   - Pop from stack and check if it matches the closing bracket
   - Return false if they don't match
5. After processing all characters, return true if stack is empty, false otherwise.

**Why this works**:
- Stack ensures we process brackets in LIFO order
- Matches the natural nesting behavior of parentheses
- Handles all edge cases properly

## Complexity Analysis
- **Time Complexity**: O(n) - Single pass through the string
- **Space Complexity**: O(n) - Stack storage in worst case

## Key Insights
- Stack is perfect for matching/balancing problems
- Must check stack emptiness before popping
- All brackets must be matched for valid string

## Solutions in Different Languages

### Python
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                stack.append(char)
        
        return not stack
```

### JavaScript
```javascript
var isValid = function(s) {
    const stack = [];
    const mapping = {')': '(', '}': '{', ']': '['};
    
    for (let char of s) {
        if (char in mapping) {
            if (!stack.length || stack.pop() !== mapping[char]) {
                return false;
            }
        } else {
            stack.push(char);
        }
    }
    
    return !stack.length;
};
```

## Test Cases
```
Test Case 1: s = "()" → true
Test Case 2: s = "()[]{}" → true
Test Case 3: s = "(]" → false
Test Case 4: s = "([)]" → false
Test Case 5: s = "{[]}" → true
Test Case 6: s = "" → true
Test Case 7: s = "[" → false
```

## Edge Cases
1. Empty string (valid)
2. Single character (invalid)
3. Only opening brackets (invalid)
4. Only closing brackets (invalid)
5. Mixed valid and invalid patterns