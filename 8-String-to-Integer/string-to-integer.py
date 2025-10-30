class Solution:
    def myAtoi(self, s: str) -> int:
        i, n = 0, len(s)
        f = 1
        num = 0

        while i < n and s[i] == ' ':
            i += 1

        if i < n and s[i] == '-':
            f = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            if num > 2**31 - 1 and f == 1:
                return 2**31 - 1
            elif num > 2**31 and f == -1:
                return -2**31
            i += 1

        return f * num
