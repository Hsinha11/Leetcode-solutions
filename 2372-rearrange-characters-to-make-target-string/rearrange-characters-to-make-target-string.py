class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        d1 = {}
        d2 = {}
        for i in target:
            d1[i] = 1 + d1.get(i,0)
        for i in s:
            d2[i] = 1 + d2.get(i,0)
        m = 10**9
        for i in d1:
            if i in d2:
                m = min(d2[i]//d1[i],m)
            else:
                return 0
        return m