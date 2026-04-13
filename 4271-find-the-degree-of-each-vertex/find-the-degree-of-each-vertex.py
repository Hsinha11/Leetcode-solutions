class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        return [sum(x) for x in matrix]