class Solution:
    def numSub(self, s: str) -> int:
        c = 0
        group = 0
        for i in s:
            if i=='1':
                group+=1
            else:
                c+= (group*(group+1))//2
                group=0
        c+= (group*(group+1))//2
        return c%(10**9+7)
