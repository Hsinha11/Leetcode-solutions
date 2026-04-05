class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x=0
        y=0
        for i in moves:
            if i =="U":
                y+=1
            if i=="D":
                y-=1
            if i=="L":
                x-=1
            if i=="R":
                x+=1
        return x==0 and y==0
        