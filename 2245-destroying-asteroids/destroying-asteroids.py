class Solution:
    def asteroidsDestroyed(self, mass: int, ast: List[int]) -> bool:
        m = mass
        ast.sort()
        for i in ast:
            if i>m:
                return False
            else:
                m+=i
        return True