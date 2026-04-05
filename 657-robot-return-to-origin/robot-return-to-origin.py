class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U')==moves.count('D') and moves.count('R')==moves.count('L')
        