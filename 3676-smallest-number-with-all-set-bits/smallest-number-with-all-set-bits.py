class Solution:
    def smallestNumber(self, n: int) -> int:
        nu = n
        bits = 0
    
        while nu > 0:
            bits += 1
            nu >>= 1
    
        i = 0
        while i < bits:  
            if not (n & (1 << i)):  
                n |= (1 << i)       
            i += 1
    
        return n