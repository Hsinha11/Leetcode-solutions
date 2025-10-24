class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        f=True
        c=n+1
        while f:
            d={}
            tem = c
            while tem:
                a = tem%10
                d[a] = d.get(a,0)+1
                tem = tem//10
            valid = True
            for i in d:
                if d[i]!=i:
                    valid=False
                    c+=1
                    break
                    # d={}
            if valid:
                return c