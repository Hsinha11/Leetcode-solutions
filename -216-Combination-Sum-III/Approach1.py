from itertools import combinations
from typing import List
class Solution:
   def combinationSum3(self, k: int, n: int) -> List[List[int]]:
       ans = []
       for c in combinations(range(1,10),k):
           if sum(c)==n:
               ans.append(c)
       return ans