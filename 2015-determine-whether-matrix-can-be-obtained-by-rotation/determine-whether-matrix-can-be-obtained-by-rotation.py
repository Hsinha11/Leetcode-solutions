class Solution:
    def findRotation(self, m: List[List[int]], target: List[List[int]]) -> bool:
        if m==target:
            return True
        for i in range(3):
            for i in range(len(m)):
                for j in range(i+1,len(m)):
                    m[i][j],m[j][i]=m[j][i],m[i][j]
            for i in m:
                i.reverse()
            if m==target:
                return True
        return False