class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        ans=0
        for i in range(num1,num2+1):
            s = str(i)
            for x in range(len(s)):
                if x>0 and x<len(s)-1:
                    if int(s[x])>int(s[x-1]) and int(s[x])>int(s[x+1]):
                        ans+=1
                    if int(s[x])<int(s[x-1]) and int(s[x])<int(s[x+1]):
                        ans+=1    
        return ans