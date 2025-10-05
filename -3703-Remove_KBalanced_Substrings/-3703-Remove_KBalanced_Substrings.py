def removeKBalancedSubstrings(s: str, k: int) -> str:
    while True:
        stack = []
        remove = [False] * len(s)
        count = 0
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
            # Check for k-balanced substring
            if len(stack) >= k and ch == ')':
                # Check if previous k ')' exist
                if i - k + 1 >= 0 and all(s[j] == ')' for j in range(i - k + 1, i + 1)):
                    # Check for k '(' before these ')'
                    start = i - 2 * k + 1
                    if start >= 0 and all(s[j] == '(' for j in range(start, start + k)):
                        for j in range(start, i + 1):
                            remove[j] = True
                        count += 1
        if count == 0:
            break
        s = ''.join([ch for i, ch in enumerate(s) if not remove[i]])
    return s

# Example usage:
# print(removeKBalancedSubstrings("(())", 1))      # Output: ""
# print(removeKBalancedSubstrings("(()(", 1))      # Output: "(("
# print(removeKBalancedSubstrings("((()))()()()", 3))  # Output: "()()()"