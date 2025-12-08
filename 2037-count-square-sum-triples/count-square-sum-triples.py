class Solution:
    def countTriples(self, n: int) -> int:
        squares = set([x**2 for x in range(1,n+1)])
        c = 0
        print(squares)
        for i in squares:
            for j in squares:
                s = math.sqrt(i+j)
                if int(s)==s and s<=n:
                    c+=1
        return c