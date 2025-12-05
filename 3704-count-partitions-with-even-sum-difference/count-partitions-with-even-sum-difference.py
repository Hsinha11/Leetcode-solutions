class Solution:
    def countPartitions(self, l: List[int]) -> int:
        c =0 
        for i in range(1,len(l)):
            print(l[:i],l[i:])
            if abs(sum(l[:i]) - sum(l[i:]))%2==0:
                c+=1
        return c