from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n < k or n > 45: return []
        
        def dfs(i, j, l, lst):
            if j == 0 and l == k:
                res.append(lst.copy())
                return
            
            if j < 0 or i > 9 or l == k: return

            lst.append(i)
            dfs(i + 1, j - i, l + 1, lst)
            lst.pop()
            dfs(i + 1, j, l, lst)
        
        res = []
        dfs(1, n, 0, [])
        return res
