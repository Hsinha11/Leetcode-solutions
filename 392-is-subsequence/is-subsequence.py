class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        # j=0
        if s=="":
            return True
        for j in range(len(t)):
            
            if s[i]==t[j]:
                i+=1
            if i==len(s):
                return True
        
        return False