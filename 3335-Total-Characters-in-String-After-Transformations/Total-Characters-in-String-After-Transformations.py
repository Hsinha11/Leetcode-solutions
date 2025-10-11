class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        count = [0] * 26 # counter array for a....z

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        for _ in range(t):
            new_count = [0] * 26
            for i in range(26):
                if count[i] == 0:
                    continue
                if i == 25: # 'z'
                    new_count[0] = (new_count[0] + count[i]) % mod # a
                    new_count[1] = (new_count[1] + count[i]) % mod # b
                else:
                    new_count[i + 1] = (new_count[i + 1] + count[i]) % mod
            count = new_count

        return sum(count) % mod