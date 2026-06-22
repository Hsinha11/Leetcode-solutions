class Solution:
    def maxDistance(self, moves: str) -> int:
        netup = 0
        netleft = 0
        dash =0
        for i in moves:
            if i=='D':
                netup-=1
            elif i=='U':
                netup+=1
            elif i=='L':
                netleft-=1
            elif i=='R':
                netleft+=1
            elif i=='_':
                dash+=1
        return abs(netup)+abs(netleft) + dash
