# Recursive code  || gives tle 
# class Solution:
#     def findRotateSteps(self, ring: str, key: str) -> int:
#         def f(r,k):
#             if k == len(key):
#                 return 0
#             res = float("inf")
#             for i,c in enumerate(ring):
#                 if c == key[k]:
#                     min_dist = min(
#                         abs(r-i), # between 
#                         len(ring)- abs(r-i) #around
#                     )
#                     res = min(res , min_dist + 1 + f(i,k+1))
#             return res
#         return f(0,0)
        
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        cache ={}
        def f(r,k):
            if k == len(key):
                return 0
            if (r,k) in cache:
                return cache[(r,k)]
            res = float("inf")
            for i,c in enumerate(ring):
                if c == key[k]:
                    min_dist = min(
                        abs(r-i), # between 
                        len(ring)- abs(r-i) #around
                    )
                    res = min(res , min_dist + 1 + f(i,k+1))
            cache[(r,k)]=res
            return res
        return f(0,0)
        