class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            c = 1
            temp = n
            while temp:
                c*=temp%10
                temp//=10
            if c%t==0:
                return n
            else:
                n+=1